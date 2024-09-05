from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class UserRgistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'password', 'user_type', 'username']