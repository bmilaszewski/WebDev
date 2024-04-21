from django.db import models

class TeachingAssistant(models.Model):
    name = models.CharField(max_length=100, default='')
    hours_of_operation = models.CharField(max_length=100, default='')
    room_number = models.CharField(max_length=10, default='')
    class_name = models.CharField(max_length=50, default='')  # New field for class

    def __str__(self):
        return self.name
    
