from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# --- NEW CUSTOM REGISTRATION FORM ---
# This form now correctly inherits ALL fields from the base form
# and just ADDS the email field.
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta): # <-- THIS LINE IS THE FIX
        model = User
        # This line now adds 'email' to all the existing fields
        fields = UserCreationForm.Meta.fields + ('email',) 

# --- EXISTING PROFILE FORM ---
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile_no', 'gender', 'address', 'postal_code', 'state']