from django.contrib import admin
from .models import TeachingAssistant

class TeachingAssistantAdmin(admin.ModelAdmin):
    list_display = ('name', 'hours_of_operation', 'room_number', 'class_name')  # Add 'class_name' here

admin.site.register(TeachingAssistant, TeachingAssistantAdmin)