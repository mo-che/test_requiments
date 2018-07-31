from __future__ import unicode_literals
from django.db import models

class Person(models.Model):
	name=models.CharField(max_length=100)
	image=models.ImageField(upload_to='images',default='\images\icon-user-default.png')
	description=models.CharField(max_length=100,blank=True,null=True)
	def __unicode__(self):
		return u"%s"%(self.name)