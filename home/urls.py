# urls.py in your app (e.g., home)
from . import views
from django.contrib import admin
from django.urls import path, include
from CareConnect.admin import custom_admin_site
from patients.views import patient_detail , patient_update , patient_delete , patient_list , patient_create
from feedback.views import view_feedback, submit_feedback

urlpatterns = [
    path('', views.home, name='home'),  # Set as the homepage
    path('about/', views.about, name='about')
    # path('admin/', custom_admin_site.urls, name='admin_pg'),
]
