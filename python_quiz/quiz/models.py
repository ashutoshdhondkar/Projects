from django.db import models

# Create your models here.
class Questions(models.Model):
	question = models.TextField()
	
	option_1 = models.CharField(max_length = 300)
	option_2 = models.CharField(max_length = 300)
	option_3 = models.CharField(max_length = 300)
	option_4 = models.CharField(max_length = 300)

	answer = models.IntegerField()
	def __str__(self):
		return str(self.id)

class Registered_Users(models.Model):
	username = models.CharField(max_length = 20 , unique=True)

	password = models.CharField(max_length = 100)

	email_id = models.CharField(max_length = 100)

	phone_no = models.CharField(max_length = 10, default = None)

	def __str__(self):
		return self.username