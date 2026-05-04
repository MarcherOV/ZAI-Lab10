from django import forms
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['subject', 'description', 'module', 'attachment']
        # 'date_reported' заповнюється автоматично, 'author' підставляється у view з request.user