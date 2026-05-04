from django import forms
from offer.models import Category, Course

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['parent', 'name', 'is_published', 'order']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['category', 'order', 'number', 'title', 'description', 'price', 'hours', 'is_published']