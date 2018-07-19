from django.db import models

# Create your models here.
class TodoDB(models.Model):
    task = models.CharField(max_length=50)
    
    complete = models.BooleanField(default=False)