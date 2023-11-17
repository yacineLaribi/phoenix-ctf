from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(ScrumUser)
class ScrumUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'denorm_score')
    # Add any other fields you want to display in the admin list view

@admin.register(UserContent)
class UserContentAdmin(admin.ModelAdmin):
    list_display = ('author','text', 'denorm_score')
