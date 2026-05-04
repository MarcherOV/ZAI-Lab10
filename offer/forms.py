from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['course', 'first_name', 'last_name', 'phone', 'email', 'rodo_consent']