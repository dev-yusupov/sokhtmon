from django.db import models

# Create your models here.

class Currency(models.Model):
	id = models.AutoField(primary_key=True)
	current_currency = models.IntegerField()

	def __int__(self):
		return self.current_currency

class Post(models.Model):
	id = models.AutoField(primary_key=True)
	first = models.FileField(upload_to="post")
	second = models.FileField(upload_to="post")
	third = models.FileField(upload_to="post")


class Contact(models.Model):
	id = models.AutoField(primary_key=True)
	phone_number = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	address = models.CharField(max_length=250)
