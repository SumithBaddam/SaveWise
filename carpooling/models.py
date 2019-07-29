from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

'''
class User(models.Model):
	name = models.CharField(max_length=30)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	def __str__(self):
		return self.username
'''
	
class Vehicle(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=30)
	seats = models.IntegerField()
	vehicle_number = models.CharField(max_length=10)
	source = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)
	price=models.IntegerField(default=0)
	date = models.DateTimeField(default=datetime.now(),blank=True)

	def __str__(self):
		return self.name
		

class find_request(models.Model):
	user_requesting = models.ForeignKey(User, default=0, related_name='%(class)s_requesting')
	user = models.ForeignKey(User, default=0,  related_name='%(class)s_requested')
	latLocation = models.FloatField(default=0)
	lonLocation = models.FloatField(default=0)
	status=models.IntegerField(default=0)
	def __str__(self):
		return self.user_requesting.username + self.user.username
		
class Request(models.Model):
	def __str__(self):
		return self.user.username + self.vehicle.name
	user = models.ForeignKey(User)
	vehicle = models.ForeignKey(Vehicle,default=0)
	seats = models.IntegerField()
	status = models.IntegerField(default=0)
	
	
