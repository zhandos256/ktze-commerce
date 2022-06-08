from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_home_view, name='get_home_view'),
    path('blog/', views.get_blog_view, name='get_blog_view'),
    path('services/', views.get_services_view, name='get_services_view'),
    path('documents/', views.get_documents_view, name='get_documents_view'),
    path('contacts/', views.get_contacts_view, name='get_contacts_view'),
    path('us/', views.get_us_view, name='get_us_view'),
    path('request/', views.get_request_view, name='get_request_view'),
    path('faq/', views.get_faq_view, name='get_faq_view'),
]

