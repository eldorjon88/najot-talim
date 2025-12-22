from django.contrib import admin
from app.teachers.models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'specialty', 'experience_years', 
                    'rating', 'students_taught', 'is_active']
    list_filter = ['is_active', 'specialty']
    search_fields = ['first_name', 'last_name', 'email']
