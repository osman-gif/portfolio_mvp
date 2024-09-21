from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from instructor.models import InstructorProfile
from school.models import SchoolProfile

# Signal receiver to automatically create a profile when a new user is created
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Triggered immediately after a CustomUser instance is created.
    Based on the user_type ('instructor' or 'school'), this creates the appropriate profile:
    - InstructorProfile for 'instructor' users with a default year_of_experience value.
    - SchoolProfile for 'school' users with a default established_year value.
    """
    if created:
        if instance.user_type == 'instructor':
            # Create an InstructorProfile if the user is an instructor
            InstructorProfile.objects.create(user=instance, year_of_experience=0)
        elif instance.user_type == 'school':
            # Create a SchoolProfile if the user is a school
            SchoolProfile.objects.create(user=instance, established_year=2)

# Signal receiver to automatically save the user profile when the user is updated
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    """
    Triggered after a CustomUser instance is saved. Ensures that the associated profile 
    (InstructorProfile or SchoolProfile) is also saved if it exists.
    """
    if instance.user_type == 'instructor' and hasattr(instance, 'instructorprofile'):
        # Save the instructor profile if it exists
        instance.instructorprofile.save()
    elif instance.user_type == 'school' and hasattr(instance, 'schoolprofile'):
        # Save the school profile if it exists
        instance.schoolprofile.save()
