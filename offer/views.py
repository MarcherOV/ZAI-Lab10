from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Course
from .forms import RegistrationForm

def offer_main(request):
    categories = Category.objects.filter(is_published=True)
    return render(request, 'offer/categories.html', {'categories': categories})

def offer_category(request, kategoria):
    category = get_object_or_404(Category, name=kategoria)
    courses = Course.objects.filter(category=category, is_published=True)
    return render(request, 'offer/courses.html', {'courses': courses, 'category': category})

def offer_course(request, kategoria, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'offer/course_detail.html', {'course': course})

# Представлення для Register (можна розмістити у головному файлі проекту або тут)
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'offer/success.html', {'msg': 'Rejestracja pomyślna'})
    else:
        form = RegistrationForm()
    return render(request, 'offer/register_form.html', {'form': form})