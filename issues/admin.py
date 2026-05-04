from django.contrib import admin
from .models import Issue

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('subject', 'author', 'module', 'date_reported')
    list_filter = ('module', 'date_reported')
    search_fields = ('subject', 'description', 'author__username')
    readonly_fields = ('date_reported',)