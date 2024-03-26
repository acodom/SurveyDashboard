#report/urls.py
from django.urls import path
from . import views
from .views import chart_view

urlpatterns = [
    path('report/', views.report_view, name='report'),
    path('chart/', chart_view, name='chart'),
]
