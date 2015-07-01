from django.contrib.auth.models import User
from django.db import models

class Employee(models.Model):
	user = models.OneToOneField(User, related_name='user')
	middle_name = models.CharField('Drugie imie', max_length=200)
	pesel = models.CharField('Pesel', max_length=11)
	id_number = models.CharField('Nr dowodu', max_length=9)
	street = models.CharField('Adres', max_length=200)
	city = models.CharField('Miejscowosc', max_length=200)
	postcode = models.CharField('Kod pocztowy', max_length=200)
	country = models.CharField('Kraj', max_length=200, default='Polska')
	
	class Meta:
		verbose_name = 'dane dodatkowe'
		verbose_name_plural = 'dane dodatkowe'
	
	def __str__(self):
		return self.user.username
