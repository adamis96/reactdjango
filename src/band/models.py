from django.db import models
import datetime
# Create your models here.

class Band(models.Model):
	name = models.CharField(max_length=128, null=False, blank=False, unique=True)
	date_added = models.DateField(default=datetime.datetime.now())
	image = models.CharField(max_length=255, null=True, blank=True)
	bio = models.TextField(max_length=5000, null=True, blank=True)

	def __unicode__(self):
	 	return self.name
	def __str__(self):
	 	return self.name

