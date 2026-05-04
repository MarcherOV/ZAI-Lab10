from django.db import models
from django.contrib.auth.models import User

class Issue(models.Model):
    MODULE_CHOICES = [
        ('offer', 'Oferta'),
        ('offer-mng', 'Zarządzanie ofertą'),
        ('register', 'Rejestracja'),
    ]

    date_reported = models.DateTimeField(auto_now_add=True, verbose_name="Data i godzina zgłoszenia")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor zgłoszenia")
    subject = models.CharField(max_length=200, verbose_name="Temat zgłoszenia")
    description = models.TextField(verbose_name="Treść/opis problemu")
    module = models.CharField(max_length=50, choices=MODULE_CHOICES, verbose_name="Moduł aplikacji")
    attachment = models.FileField(upload_to='issues_attachments/', null=True, blank=True, verbose_name="Opcjonalne załączniki")