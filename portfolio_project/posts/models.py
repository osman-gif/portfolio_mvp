from django.db import models
from school.models import SchoolProfile

# Create your models here.

class JobPost(models.Model):
    # school = models.ForeignKey(School, on_delete=models.CASCADE)
    CHOICES = (
        ('math','Math'), ('english','English')
    )
    subject = models.CharField(max_length=50,choices=CHOICES, default= 'Math')
    school = models.ForeignKey(SchoolProfile, on_delete=models.CASCADE, null=True, blank=True)
    position_title = models.CharField(max_length=255)
    description = models.TextField()
    requirements_summary = models.TextField()
    application_deadline = models.DateField()
    salary_range = models.CharField(max_length=50)
    employment_type = models.CharField(max_length=50, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position_title