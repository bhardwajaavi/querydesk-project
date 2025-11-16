from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# --- NEW CUSTOM REGISTRATION FORM (The fix) ---
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',) 

# --- EXISTING PROFILE FORM ---
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile_no', 'gender', 'address', 'postal_code', 'state']