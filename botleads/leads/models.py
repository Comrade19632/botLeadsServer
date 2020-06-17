from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=True, region='RU')
    email = models.EmailField(max_length=100, blank=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE, null=True)
