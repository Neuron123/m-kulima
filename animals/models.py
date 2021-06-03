from django.db import models
from datetime import datetime
from hasianda.models import Hasianda

# Create your models here.
class Animal (models.Model):
	date = models.DateTimeField('date added', default = datetime.now)
	category=models.CharField(max_length=200,blank=True, null=True)
	animaltype=models.CharField(max_length=200,blank=True, null=True)
	breed=models.CharField(max_length=200,blank=True,null=True)
	number=models.CharField(max_length=200,blank=True, null=True)
	calved=models.BooleanField(blank=True, null=True)
	buyingprice=models.IntegerField(default=0,blank=True, null=True)
	currency=models.CharField(max_length=200,blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	Email_Address = models.EmailField(max_length=1000,blank=True, null=True)
	# file will be uploaded to MEDIA_ROOT/uploads
	profilepic=models.FileField(upload_to='uploads/',blank=True, null=True)
	Farm_Name = models.CharField(max_length=200)
	#land = models.ForeignKey(Hasianda, on_delete=models.CASCADE, related_name="farmlist",default=1)




	def __str__(self):
		return self.category

