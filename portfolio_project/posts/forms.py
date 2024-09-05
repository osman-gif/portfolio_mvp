from .models import JobPost
from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = JobPost
        fields = '__all__'