from django.contrib import admin

# Register your models here.

from .models import University, Student

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'short_name', 'creation_date')

admin.site.register(University, UniversityAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'university', 'birth_date', 'enrollment_year')

admin.site.register( Student,  StudentAdmin)