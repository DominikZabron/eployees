#-*- coding: utf-8 -*-

from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models

@python_2_unicode_compatible
class Employee(models.Model):
	user = models.OneToOneField(User, parent_link=True, related_name='user')
	position = models.CharField('Stanowisko', max_length=255, blank=True)
	middle_name = models.CharField('Drugie imię', max_length=200, blank=True)
	pesel = models.CharField('Pesel', max_length=11, blank=True)
	id_number = models.CharField('Nr dowodu', max_length=9, blank=True)
	street = models.CharField('Adres', max_length=200, blank=True)
	city = models.CharField('Miejscowość', max_length=200, blank=True)
	postcode = models.CharField('Kod pocztowy', max_length=200, blank=True)
	country = models.CharField('Kraj', max_length=200, default='Polska', blank=True)
	avatar = models.FileField(upload_to='avatars',
		default='/media/avatars/pawn.jpg')
		
	def __str__(self):
		return self.user.username	
		
	class Meta:
		verbose_name = 'dane pracownika'
		verbose_name_plural = 'dane osobowe'

def create_employee(sender, instance, created, **kwargs):
	if created:
		Employee.objects.create(user=instance)

post_save.connect(create_employee, sender=User)



@python_2_unicode_compatible
class Qualifications(models.Model):
	name = models.CharField('nazwa', max_length=255)
	ordinal = models.PositiveIntegerField('LP')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'uprawnienie'
		verbose_name_plural = 'uprawnienia'

@python_2_unicode_compatible
class QualificationsEmployee(models.Model):
	employee = models.ForeignKey(Employee, verbose_name='pracownik')
	qualifications = models.ForeignKey(Qualifications,
		verbose_name='uprawnienia')
	expiry_date = models.DateField('wygasają')

	def __str__(self):
		return self.qualifications.name

	class Meta:
		verbose_name = 'uprawnienie'
		verbose_name_plural = 'uprawnienia'
		

