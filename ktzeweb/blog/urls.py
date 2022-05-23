from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_blog_view, name='get_blog_view'),
]

