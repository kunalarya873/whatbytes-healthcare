from django.db import models
from accounts.models import User

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)