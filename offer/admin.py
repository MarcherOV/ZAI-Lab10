from django.contrib import admin
from .models import Category, Course, Registration

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_published', 'parent')
    list_filter = ('is_published', 'parent')
    search_fields = ('name',)
    ordering = ('order', 'name')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'hours', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'number', 'description')
    list_editable = ('price', 'is_published')

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'course', 'status', 'date_registered')
    list_filter = ('status', 'course', 'date_registered')
    search_fields = ('last_name', 'email', 'phone')
    ordering = ('-date_registered',)