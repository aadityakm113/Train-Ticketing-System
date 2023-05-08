from django.db import models

# Create your models here.
from django.forms import ModelForm,Textarea
class Users_Login(models.Model):
	# these are  mysq col names
	user_name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	pwd=models.CharField(max_length=100)
