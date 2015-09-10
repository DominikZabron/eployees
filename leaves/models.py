#-*- coding: utf-8 -*-

from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models
from datetime import date

@python_2_unicode_compatible
class Leave(models.Model):
	user = models.OneToOneField(User, primary_key=True, parent_link=True, related_name='leave', verbose_name='Pracownik')
	available_days = models.IntegerField('dni urlopu kalendarzowego', default=26)
	
	def first_name(self):
		return self.user.first_name
	first_name.short_description = 'Imię'
	
	def last_name(self):
		return self.user.last_name
	last_name.short_description = 'Nazwisko'

	def _days_left(self):
		lr = LeaveRequest.objects.filter(leave=self.user.id).filter(
			start_date__year=date.today().year).filter(
			status='a')
		days = 0
		for request in lr:
			days += request.days
		return self.available_days - days

	_days_left.short_description = 'dni urlopu pozostało'
	days_left =	property(_days_left)

	def _days_used(self):
		return self.available_days - self._days_left()

	_days_used.short_description = 'dni urlopu wykorzystane'
	days_used = property(_days_used)
	
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

@python_2_unicode_compatible		
class LeaveRequest(models.Model):
	leave = models.ForeignKey(Leave, verbose_name='Pracownik')
	start_date = models.DateField('poczatek urlopu')
	end_date = models.DateField('koniec urlopu')
	year = models.IntegerField('dotyczy roku kalendarzowego')
	days = models.IntegerField('dni urlopu')
	status = models.CharField('decyzja', max_length=1, choices=STATUS_CHOICES, default='w')
	
	def __str__(self):
		return ("%s %s" % (self.leave.user.last_name, self.leave.user.first_name))
		
	class Meta:
		verbose_name = 'wniosek o urlop'
		verbose_name_plural = 'wnioski urlopowe'
	

