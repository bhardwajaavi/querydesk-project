from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")
        # We will handle passwords separately in the template
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile_no', 'gender', 'address', 'postal_code', 'state']