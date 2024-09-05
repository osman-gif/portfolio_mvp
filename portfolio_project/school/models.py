from django.db import models
from accounts.models import CustomUser


# Create your models here.
class SchoolProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255)
    school_type = models.CharField(max_length=50)
    description = models.TextField()
    established_year = models.PositiveIntegerField()
    website = models.URLField(blank=True, null=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - School"
