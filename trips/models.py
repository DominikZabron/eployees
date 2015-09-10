#-*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
import datetime
from assets.models import Car

@python_2_unicode_compatible
class BusinessTrip(models.Model):
	purpose = models.CharField('Cel wyjazdu', max_length=255)
	begin_date = models.DateField('Rozpoczęcie')
	description = models.TextField('Opis', blank=True)
	
	def __str__(self):
		return self.purpose
		
	class Meta:
		verbose_name = 'Delegacja'
		verbose_name_plural = 'Delegacje'


STATUS_CHOICES = (
	('w', 'Oczekuje'),
	('a', 'Zaakceptowany'),
	('r', 'Odrzucony'),
)
	
@python_2_unicode_compatible
class BusinessTripEmployee(models.Model):
	employee = models.ForeignKey(User, verbose_name='Pracownik')
	business_trip = models.ForeignKey(BusinessTrip, verbose_name='Delegacja')
	estimated_cost = models.DecimalField('Szacunkowy koszt [zł]', max_digits=9, decimal_places=2)
	status = models.CharField('Decyzja', max_length=1, choices=STATUS_CHOICES, default='w')

	def _trip_count(self):
		t = BusinessTripEmployee.objects.filter(status='a').count()
		return t

	_trip_count.short_description = 'odbytych delegacji'
	trip_count = property(_trip_count)

	def _settlement_count(self):
		s = BusinessTripSettlement.objects.filter(status='a').count()
		return s

	_settlement_count.short_description = 'rozliczonych delegacji'
	settlement_count = property(_settlement_count)
	
	def __str__(self):
		return "{1} - {0}".format(self.employee.username, self.business_trip.__str__())
		
	class Meta:
		verbose_name = 'Wyjazd służbowy'
		verbose_name_plural = 'Wyjazdy służbowe'


TRANSPORT_TYPE = (
	('c', 'samochód firmowy'),
	('o', 'samochód prywatny'),
	('r', 'pasażer'),
	('p', 'komunkacja publiczna'),
	('t', 'pociąg'),
	('a', 'samolot'),
)

@python_2_unicode_compatible
class BusinessTripRoute(models.Model):
	trip = models.ForeignKey(BusinessTripEmployee, verbose_name='Wyjazd')
	begin = models.CharField('Miejsce początkowe', max_length=255)
	begin_time = models.DateTimeField('Początek wyjazdu')
	end = models.CharField('Miejsce docelowe', max_length=255)
	end_time = models.DateTimeField('Koniec wyjazdu')
	transportation = models.CharField('Środek transportu', max_length=1, choices=TRANSPORT_TYPE)

	def __str__(self):
		return u"{0} - {1}".format(self.begin, self.end)
		
	class Meta:
		verbose_name = 'Przejazd'
		verbose_name_plural = 'Przejazdy'


SETTLEMENT_CHOICES = (
	('w', 'Oczekuje'),
	('a', 'Rozliczono'),
	('r', 'Odrzucono'),
)

@python_2_unicode_compatible
class BusinessTripSettlement(models.Model):
	trip = models.ForeignKey(BusinessTripEmployee, verbose_name='Wyjazd')
	status = models.CharField('Decyzja', max_length=1, choices=SETTLEMENT_CHOICES, default='w')
	
	def __str__(self):
		return self.trip.__str__()
		
	class Meta:
		verbose_name = 'Rozliczenie'
		verbose_name_plural = 'Rozliczenia'


BASE_ALLOWANCE = 30
COMMUTE_QUOTE = 0.2
ACCOMODATION_QUOTE = 1.5

@python_2_unicode_compatible
class BusinessTripAllowance(models.Model):
	settlement = models.ForeignKey(BusinessTripSettlement, verbose_name="Rozliczenie")
	begin_time = models.DateTimeField('Początek')
	end_time = models.DateTimeField('Koniec')
	is_first_day = models.BooleanField('Pierwszy dzień delegacji', default=True)
	is_breakfast = models.BooleanField('Śniadanie')
	is_dinner = models.BooleanField('Obiad')
	is_supper= models.BooleanField('Kolacja')
	is_commute_lump = models.BooleanField('Ryczałt za dojazdy')
	is_accomodation_lump = models.BooleanField('Ryczałt za noclegi')

	def _commute_lump(self, base=BASE_ALLOWANCE, quote=COMMUTE_QUOTE):
		return base * quote if self.is_commute_lump else 0
	
	_commute_lump.short_description = 'Ryczałt za dojazdy'
	commute_lump = property(_commute_lump)


	def _accomodation_lump(self, base=BASE_ALLOWANCE, quote=ACCOMODATION_QUOTE):
		return base * quote if self.is_accomodation_lump else 0

	_accomodation_lump.short_description = 'Ryczałt za noclegi'
	accomodation_lump = property(_accomodation_lump)

	def _board_quote(self):
		quote = 1

		if self.is_breakfast:
			quote -= 0.25
		if self.is_dinner:
			quote -= 0.5  
		if self.is_supper:
			quote -= 0.25 

		return quote

	def _duration_quote(self):

		try:
			duration = abs(self.end_time - self.begin_time).total_seconds() / 3600
		except:
			duration = 0	#Adding new blank entity result in error if not set

		if self.is_first_day:
			if duration > 8 and duration <= 12:
				quote = 0.5
			elif duration > 12:
				quote = 1
			else:
				quote = 0
		else:
			if duration <= 8:
				quote = 0.5
			else:
				quote = 1

		return quote

	def _allowance(self, base=BASE_ALLOWANCE):
		return base * self._board_quote() * self._duration_quote()

	_allowance.short_description = 'Dieta'
	allowance = property(_allowance)

	def _total_allowance(self):
		return self._allowance() + self._commute_lump() + self._accomodation_lump()

	_total_allowance.short_description = 'Ogółem'
	total_allowance = property(_total_allowance)

	def __str__(self):
		return "{0} - {1}".format(self.begin_time.strftime('%Y-%m-%d %H:%M'),
			self.end_time.strftime("%Y-%m-%d %H:%M"))

	class Meta:
		verbose_name = 'Dieta'
		verbose_name_plural = 'Diety'


@python_2_unicode_compatible
class BusinessTripInvoice(models.Model):
	settlement = models.ForeignKey(BusinessTripSettlement,
		verbose_name="Wyjazd")
	name = models.CharField('Nazwa', max_length=255)
	amount = models.DecimalField('Kwota', max_digits=9, decimal_places=2,
		default=0) # Milage needs default or blank to work 
	desc = models.TextField('Opis', blank=True)

	def __str__(self):
		return u"{0} - {1}".format(self.name, self.amount)

	class Meta:
		abstract = True

class BusinessTripInvoiceFare(BusinessTripInvoice):
	route = models.ForeignKey(BusinessTripRoute, verbose_name='Trasa')

	class Meta:
		verbose_name = 'Koszt podróży'
		verbose_name_plural = 'Koszty podróży'

class BusinessTripInvoiceAccomodation(BusinessTripInvoice):
	overnight = models.ForeignKey(BusinessTripAllowance, verbose_name='Nocleg')

	class Meta:
		verbose_name = 'Koszt noclegu'
		verbose_name_plural = 'Koszty noclegu'

class BusinessTripInvoiceOther(BusinessTripInvoice):
	pass

	class Meta:
		verbose_name = 'Inny'
		verbose_name_plural = 'Pozostałe koszty'

# Engine size 900 cm3
ENGINE_MARGIN = 900
SMALL_ENGINE = 0.5214
BIG_ENGINE = 0.8358

class BusinessTripInvoiceMilage(BusinessTripInvoice):
	route = models.ForeignKey(BusinessTripRoute, verbose_name='Trasa')
	car = models.ForeignKey(Car, verbose_name='Pojazd')
	distance = models.DecimalField('Odległość [km]', max_digits=9, decimal_places=2)
	
	def value(self, small_quote=SMALL_ENGINE, big_quote=BIG_ENGINE,
		margin=ENGINE_MARGIN):

		if self.car.engine_capacity < margin:
			return "{:9,.2f}".format(float(self.distance) * small_quote)
		else:
			return "{:9,.2f}".format(float(self.distance) * big_quote)
	value.short_description = 'Kwota'

	def __str__(self):
		return u"{0} - {1} km".format(self.car.__str__(), self.distance)

	class Meta:
		verbose_name = 'Rejestracja przebiegu pojazdu'
		verbose_name_plural = 'Rejestracja przebiegu pojazdów'

	
