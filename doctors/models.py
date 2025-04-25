from django.db import models
from accounts.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.name} - {self.specialization}"