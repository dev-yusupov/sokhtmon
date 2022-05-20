from django.db import models

# Create your models here.
class Product(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=250)
	cover = models.FileField(upload_to='product/cover')
	cover_first = models.FileField(upload_to='product/cover')
	cover_second = models.FileField(upload_to='product/cover')
	size = models.CharField(max_length=250)
	price = models.IntegerField()
	somoni = models.BooleanField()
	ruble = models.BooleanField()
	discription = models.TextField()

	def __str__(self):
		return f"{self.id}. {self.title}"

	def delete(self, *args, **kwargs):
		self.cover.delete()
		super().delete(*args, **kwargs)
