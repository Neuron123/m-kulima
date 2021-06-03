from django.db import models
from datetime import datetime

from hasianda.models import Hasianda


# Create your models here.
class Crop (models.Model):
	Date = models.DateTimeField('date added', default = datetime.now)
	Crop_Name = models.CharField(max_length=200)
	Crop_Variety = models.CharField(max_length=200)
	Date_Of_Planting = models.DateTimeField('date planted', default = datetime.now)
	Expected_Date_Of_Havest = models.DateTimeField('estimated havest date', default = datetime.now)
	Quantity_Of_Seeds = models.CharField(max_length=200)
	Cost_Of_Seeds = models.DecimalField(max_digits=8, decimal_places=2,default=1)
	Description = models.TextField(blank=True, null=True)
	Email_Address = models.EmailField(max_length=1000)
	Farm_name = models.CharField(max_length=200)
	land = models.ForeignKey(Hasianda, on_delete=models.CASCADE, related_name="landlist",default=1)
	


	def __str__(self):
		return self.Crop_Name

