from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile_no', 'gender', 'address', 'postal_code', 'state']