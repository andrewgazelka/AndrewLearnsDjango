# Register your models here.
from django.contrib import admin
from .models import Question, Choice

admin.site.register(Question)  # Adds question to admin interface
admin.site.register(Choice)  # Adds question to admin interface