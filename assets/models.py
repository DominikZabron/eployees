from django.contrib.auth.models import User
from django.db import models

class Car(models.Model):
	name = models.CharField('Nazwa pojazdu', max_length=200)
	brand = models.CharField('Marka pojazdu', max_length=200)
	registration_number = models.CharField('Numer rejestracyjny', max_length=200)
	engine_capacity = models.IntegerField('Pojemnosc silnika')
	is_company_owned = models.BooleanField('Wlasnosc firmy')
	user = models.ForeignKey(User, verbose_name='Pracownik', null=True, blank=True)
	
	def __str__(self):
		return self.name
		
	class Meta:
		verbose_name = 'pojazd'
		verbose_name_plural = 'pojazdy'
