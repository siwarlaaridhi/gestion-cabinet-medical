from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import  MinLengthValidator,MaxLengthValidator,RegexValidator 
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
class user (AbstractUser):
      pass
number_validator=RegexValidator(
   regex=r'^\d{8}$',
   message="le numero doit contenir exactement 8 chiffres")
def birth_date_validator (d):
     if d>= timezone.localdate():
          raise ValidationError("la date doit etre anterieur que la date d'aujourdhui")
     
class Doctor (User):
    license_number= models.CharField(max_length=6, unique=True, validators= [MinLengthValidator(6),MaxLengthValidator(6)] )
    phone= models.CharField(max_length=8,validators=[number_validator])
    Specialties =models.ManyToManyField("AccountApp.specialty", related_name="doctors")
class Patient (User):
     national_id= models.CharField(max_length=8,unique=True,validators=[number_validator])
     phone=models.CharField(max_length=8,validators=[number_validator])
     birth_date= models.DateField(birth_date_validator)

class Specialty (models.Model):
     id = models.AutoField(primary_key=True)
     name= models.CharField(max_length=50,unique=True )