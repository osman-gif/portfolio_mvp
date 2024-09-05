from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from school.models import SchoolProfile
from instructor.models import InstructorProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender,  instance, created, **kwargs):
    if created:
        if instance.user_type == 'instructor':
            print('instructor profile')
            InstructorProfile.objects.create(user=instance, year_of_experience=0)
        else:
            SchoolProfile.objects.create(user=instance, established_year=2)

def save_user_profile(sender, instance, **kwargs):
    print('save')
    if instance.user_type=='instructor' and hasattr(instance, 'instructorprofile'):
        instance.instructorprofile.save()
    elif instance.user_type=='school' and hasattr(instance, 'schoolprofile'):
        instance.schoolprofile.save()
