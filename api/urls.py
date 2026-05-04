from django.urls import path
from . import views

urlpatterns = [
    # Ендпоінти з таблиці
    path('formTemplates/', views.FormTemplateView.as_view()),
    path('messageTemplates/', views.MessageTemplateView.as_view()),
    path('categories/', views.CategoryListView.as_view()),
    path('courses/', views.CourseListView.as_view()),
    path('registers/', views.RegistrationListView.as_view()),
    path('register/', views.RegistrationCreateView.as_view()),
    path('register/<int:id>/', views.RegistrationDetailView.as_view()),
    path('problemReport/', views.ProblemReportCreateView.as_view()),
    path('problems/', views.ProblemListView.as_view()),
    
    # Генератор форм
    path('get-fields/', views.FieldListView.as_view()),
    path('save/', views.DocumentSaveView.as_view()),
    path('list/', views.DocumentListView.as_view()),
    path('load/', views.DocumentLoadView.as_view()),
]