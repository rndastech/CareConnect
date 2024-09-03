# myapp/admin.py

from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

class CustomAdminSite(admin.AdminSite):
    site_header = 'CareConnect Admin'
    site_title = 'CareConnect Admin Portal'
    index_title = 'Welcome to CareConnect Admin Portal'

# Instantiate the custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')

custom_admin_site.register(User)
custom_admin_site.register(Group)
custom_admin_site.register(Permission)
custom_admin_site.register(ContentType)
