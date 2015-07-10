#-*- coding: utf-8 -*-

from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models

@python_2_unicode_compatible
class Leave(models.Model):
	user = models.OneToOneField(User, primary_key=True, parent_link=True, related_name='leave')
	available_days = models.IntegerField('dni urlopu', default=26)
	
	def first_name(self):
		return self.user.first_name
	first_name.short_description = 'Imię'
	
	def last_name(self):
		return self.user.last_name
	last_name.short_description = 'Nazwisko'
	
	def __str__(self):
		return ("%s %s" % (self.user.last_name, self.user.first_name))
		
	class Meta:
		verbose_name = 'urlop pracownika'
		verbose_name_plural = 'urlopy pracowników'

def create_leave(sender, instance, created, **kwargs):
	if created:
		Leave.objects.create(user=instance)
		
post_save.connect(create_leave, sender=User)


STATUS_CHOICES = (
	('w', 'Oczekuje'),
	('a', 'Zaakceptowany'),
	('r', 'Odrzucony'),
)
		
class LeaveRequest(models.Model):
	leave = models.ForeignKey(Leave)
	start_date = models.DateField('poczatek urlopu')
	end_date = models.DateField('koniec urlopu')
	days = models.IntegerField('dni urlopu')
	status = models.CharField('decyzja', max_length=1, choices=STATUS_CHOICES)
	
	def __str__(self):
		return ("%s %s" % (self.leave.user.last_name, self.leave.user.first_name))
		
	class Meta:
		verbose_name = 'wniosek o urlop'
		verbose_name_plural = 'wnioski urlopowe'
	

