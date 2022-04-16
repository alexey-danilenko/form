from django.contrib import admin
from .models import MyForm

@admin.register(MyForm)
class MyFormAdmin(admin.ModelAdmin):
    pass