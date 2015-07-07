from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models

class Leave(models.Model):
	user = models.OneToOneField(User, primary_key=True, parent_link=True, related_name='user')
	available_days = models.IntegerField(default=26)
	
	def __str__(self):
		return (self.user.last_name + ' ' + self.user.first_name)
		
	class Meta:
		verbose_name = 'urlop pracownika'
		verbose_name_plural = 'urlopy pracownikow'
		
def create_leave(sender, instance, created, **kwargs):
	if created:
		Leave.objects.create(user=instance)
		
post_save.connect(create_leave, sender=User)
