#-*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

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

TRANSPORT_TYPE = (
	('p', 'komunkacja publiczna'),
	('c', 'samochód firmowy'),
	('o', 'samochód prywatny'),
	('r', 'pasażer')
)

STATUS_CHOICES = (
	('w', 'Oczekuje'),
	('a', 'Zaakceptowany'),
	('r', 'Odrzucony'),
)
	
@python_2_unicode_compatible
class BusinessTripItem(models.Model):
	employee = models.ForeignKey(User, verbose_name='Pracownik')
	business_trip = models.ForeignKey(BusinessTrip, verbose_name='Delegacja')
	trip_from = models.CharField('Miejsce początkowe', max_length=255)
	begin_time = models.DateTimeField('Początek wyjazdu')
	trip_to = models.CharField('Miejsce docelowe', max_length=255)
	end_time = models.DateTimeField('Koniec wyjazdu')
	transportation = models.CharField('Środek transportu', max_length=1, choices=TRANSPORT_TYPE)
	vehicle = models.ForeignKey('assets.Car', verbose_name='Pojazd', blank=True, null=True)
	distance = models.IntegerField('Odległość [km]')
	estimated_cost = models.DecimalField('Szacunkowy koszt [zł]', max_digits=9, decimal_places=2)
	status = models.CharField('Decyzja', max_length=1, choices=STATUS_CHOICES, default='w')
	
	def __str__(self):
		return self.employee.get_full_name()
		
	class Meta:
		verbose_name = 'Wyjazd służbowy'
		verbose_name_plural = 'Wyjazdy służbowe'

SETTLEMENT_CHOICES = (
	('w', 'Oczekuje'),
	('a', 'Rozliczono'),
	('r', 'Odrzucono'),
)
@python_2_unicode_compatible
class BusinessTripSettlement(models.Model):
	business_trip = models.ForeignKey(BusinessTrip, verbose_name='Delegacja')
	costs_all = models.DecimalField('Łączne koszty do rozliczenia', max_digits=9, decimal_places=2)
	description = models.TextField('Opis', blank=True)
	status = models.CharField('Decyzja', max_length=1, choices=SETTLEMENT_CHOICES, default='w')
	
	def __str__(self):
		return self.business_trip.__str__()
		
	class Meta:
		verbose_name = 'Rozliczenie'
		verbose_name_plural = 'Rozliczenia'
	
