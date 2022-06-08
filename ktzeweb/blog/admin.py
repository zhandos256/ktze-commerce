from django.contrib import admin
from .models import Article

admin.site.register(Article)
admin.site.site_header = "KTZ Commerce Admin Panel"