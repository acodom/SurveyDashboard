from django.urls import path
from . import views

app_name = 'authentication'  # Namespace for URL patterns

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('account/',views.account, name='account'),
    # Add other URL patterns as needed
]
