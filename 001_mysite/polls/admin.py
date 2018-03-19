# Register your models here.
from django.contrib import admin
from .models import Question

admin.site.register(Question)  # Adds question to admin interface
