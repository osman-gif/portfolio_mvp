from django.forms import ModelForm
from .models import SchoolProfile

class UpdateSchoolProfile(ModelForm):
    class Meta:
        model = SchoolProfile
        fields = '__all__'