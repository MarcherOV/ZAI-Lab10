from django import forms
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['subject', 'description', 'module', 'attachment']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }