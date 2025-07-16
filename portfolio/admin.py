from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ContactMessage

admin.site.register(ContactMessage)
admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin Portal"
admin.site.index_title = "Welcome to the Portfolio Admin Portal"