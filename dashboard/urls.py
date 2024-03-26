"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from authentication import views as auth_views_custom  # Import views from your authentication app



urlpatterns = [
    path('admin/', admin.site.urls),
    path('survey/', include('survey.urls')),
    path('register/', auth_views_custom.register, name='register'),  # URL pattern for user registration
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # URL pattern for user login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL pattern for user logout
    path('report/', include('report.urls')),
    path('account/', auth_views_custom.account, name='account'),  # Include your authentication app's URLs
    # Add other URL patterns for your project
]
