from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    pass

# Register your models with the Django Admin interface
admin.site.register(Question, QuestionAdmin)

# Optionally, create custom admin classes for more control
#class YourModel1Admin(admin.ModelAdmin):
#    list_display = ('field1', 'field2', 'field3')  # Display these fields in the list view
#    search_fields = ['field1', 'field2']  # Add search functionality
#    list_filter = ('field3',)  # Add filtering options

# admin.site.register(YourModel1, YourModel1Admin)
