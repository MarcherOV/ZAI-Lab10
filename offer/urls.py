from django.urls import path

from . import views

urlpatterns = [
    path('', views.offer_main, name='offer_main'),
    path('register/', views.register_view, name='register_view'),
    path('<str:kategoria>/', views.offer_category, name='offer_category'),
    path('<str:kategoria>/course/<int:course_id>/', views.offer_course, name='offer_course'), # Додано course_id для точності
]