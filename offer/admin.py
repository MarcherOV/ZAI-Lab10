from django.contrib import admin
from .models import Category, Course, Registration

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Поля, які відображаються в таблиці
    list_display = ('name', 'order', 'is_published', 'parent')
    # Фільтрація в правій колонці
    list_filter = ('is_published', 'parent')
    # Пошук за назвою
    search_fields = ('name',)
    # Сортування за замовчуванням
    ordering = ('order', 'name')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'hours', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'number', 'description')
    # Можливість редагувати ціну прямо зі списку (опціонально, але круто для Lab-30)
    list_editable = ('price', 'is_published')

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'course', 'status', 'date_registered')
    list_filter = ('status', 'course', 'date_registered')
    search_fields = ('last_name', 'email', 'phone')
    # Сортування від нових до старих
    ordering = ('-date_registered',)