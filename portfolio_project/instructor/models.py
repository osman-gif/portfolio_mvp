from django.db import models
from accounts.models import CustomUser

# Create your models here.

class InstructorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    year_of_experience = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - Instructor"