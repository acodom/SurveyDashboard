from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# models.py

class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text
    
    class Meta:
        app_label = 'survey'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    class Meta:
        app_label = 'survey'

    def __str__(self):
        return self.choice_text
    

class SurveyResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model for user authentication

    def __str__(self):
        return f"{self.user.username}'s response to {self.question}"