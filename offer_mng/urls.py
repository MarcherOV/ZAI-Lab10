from django.urls import path
from offer_mng import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel_main, name='panel_main'),
    path('generator/', views.generator_view, name='generator'),
    path('categ-lst/', views.categ_lst, name='categ_lst'),
    path('course-lst/', views.course_lst, name='course_lst'),
    path('categ-add/', views.categ_add, name='categ_add'),
    path('course-add/', views.course_add, name='course_add'),
]