from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')

admin.site.register(Student, StudentAdmin)