from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Hasianda (models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="farmlist",default=1)
	Date = models.DateTimeField('date added', default = datetime.now)
	Farm_Name = models.CharField(max_length=200)
	Email_Address = models.EmailField(max_length=200)
	County = models.CharField(max_length=200)
	Address = models.CharField(max_length=200)
	Size = models.CharField(max_length=200)
	Description = models.TextField(blank=True, null=True)


	def __str__(self):
		return self.Farm_Name


	
