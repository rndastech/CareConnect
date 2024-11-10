"""
URL configuration for CareConnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# CareConnect/urls.py

from django.urls import path, include
from CareConnect.admin import custom_admin_site
from patients.views import patient_detail, patient_update, patient_delete, patient_list, patient_create
from feedback.views import view_feedback, submit_feedback

urlpatterns = [
    # Custom Admin URL
    path('admin/', custom_admin_site.urls, name='admin_pg'),  # custom admin site at /admin/

    # Include app URLs
    path('', include('home.urls')),  # root path handled by home.urls
    path('patients/', include('patients.urls')),  # patients app URLs
    path('feedback/', include('feedback.urls')),  # feedback app URLs

    # Authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Django authentication system

    # Patient-specific views
    path('ehr/<int:pk>/', patient_detail, name='patient_detail'),
    path('patients/<int:pk>/edit/', patient_update, name='patient_update'),
    path('patients/<int:pk>/delete/', patient_delete, name='patient_delete'),
    path('patients/new/', patient_create, name='patient_create'),
    path('patients/', patient_list, name='patient_list'),

    # Feedback-specific views
    path('view/', view_feedback, name='view_feedback'),
    path('submit/', submit_feedback, name='submit_feedback'),
]
