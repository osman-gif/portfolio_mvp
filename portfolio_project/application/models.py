from django.db import models
from posts.models import JobPost
from instructor.models import InstructorProfile
from accounts.models import CustomUser
# Create your models here.


class Application(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.SET_NULL, null=True)
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Submitted', 'Submitted'), ('Under Review', 'Under Review'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')])
    cover_letter = models.TextField()

    def __str__(self):
        return f"Application by {self.instructor} for {self.job_post}"
