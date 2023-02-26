from .models import tckPOSMate_cashier
from django import forms


class cashierLoginForm(forms.ModelForm):
    class Meta:
        model = tckPOSMate_cashier
        fields = ['email', 'prefix']