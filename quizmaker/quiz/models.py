from django.db import models

# Create your models here.
class Register_Users(models.Model):
	username = models.CharField(max_length = 20)
	email = models.CharField(max_length = 40)
	phone = models.CharField(max_length = 10)
	password = models.CharField(max_length = 100)

	def __str__(self):
		return self.username

class Questions(models.Model):
	question = models.TextField(max_length = 300)
	option_1 = models.CharField(max_length = 300)
	option_2 = models.CharField(max_length = 300)
	option_3 = models.CharField(max_length = 300)
	option_4 = models.CharField(max_length = 300)
	#option_5 = models.CharField(max_length = 50)
	ans_key = models.IntegerField()

	def __str__(self):
		return str(self.id)

class Marks(models.Model):
	userid = models.IntegerField()
	marks = models.IntegerField()

	def __str__(self):
		return str(self.id)