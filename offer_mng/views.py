from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from offer.models import Category, Course
from .forms import CategoryForm, CourseForm

@login_required(login_url='/admin/login/')
def panel_main(request):
    return render(request, 'offer_mng/panel_main.html')

@login_required
def categ_lst(request):
    categories = Category.objects.all()
    return render(request, 'offer_mng/categ_lst.html', {'categories': categories})

@login_required
def course_lst(request):
    courses = Course.objects.all()
    return render(request, 'offer_mng/course_lst.html', {'courses': courses})

@login_required
def categ_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categ_lst')
    else:
        form = CategoryForm()
    return render(request, 'offer_mng/form_template.html', {'form': form, 'title': 'Dodaj kategorie'})

@login_required
def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_lst')
    else:
        form = CourseForm()
    return render(request, 'offer_mng/form_template.html', {'form': form, 'title': 'Dodaj szkolenie'})

@login_required
def generator_view(request):
    return render(request, 'offer_mng/generator.html')