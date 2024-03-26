# urls.py (inside the "survey" app)

from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path('survey/', views.survey_view, name='survey'),
    path('survey/success/', views.survey_success, name='survey_success'),
]
