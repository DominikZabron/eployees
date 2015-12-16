#-*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

class Car(models.Model):
	name = models.CharField('Nazwa pojazdu', max_length=200)
	brand = models.CharField('Marka pojazdu', max_length=200)
	registration_number = models.CharField('Numer rejestracyjny', max_length=200)
	engine_capacity = models.IntegerField('Pojemnosc silnika')
	is_company_owned = models.BooleanField('Wlasnosc firmy')
	next_tech_inspection = models.DateField('Przegląd ważny do', null=True, blank=True)
	user = models.ForeignKey(User, verbose_name='Pracownik', null=True, blank=True)
	
	def __str__(self):
		return self.registration_number
		
	class Meta:
		verbose_name = 'pojazd'
		verbose_name_plural = 'pojazdy'
