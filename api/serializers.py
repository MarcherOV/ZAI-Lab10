from rest_framework import serializers
from offer.models import Course, Registration, MessageTemplate
from issues.models import Issue

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'price', 'hours', 'is_published']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'subject', 'module', 'date_reported', 'description']
        read_only_fields = ['date_reported']