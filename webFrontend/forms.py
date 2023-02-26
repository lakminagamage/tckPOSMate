from .models import Profile
from django import forms


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'contact_number', 'address', 'image']