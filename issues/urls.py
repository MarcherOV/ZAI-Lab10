from django.urls import path
from . import views

urlpatterns = [
    path('', views.issue_report, name='issue_report'),
    path('problemReport/', views.problem_list, name='problem_list'),
    path('problems/<int:issue_id>/', views.problem_detail, name='problem_detail'),
]