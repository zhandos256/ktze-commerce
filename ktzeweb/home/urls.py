from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_home_view, name='get_home_view'),
    path('documents/', views.get_documents_view, name='get_documents_view'),
    path('services/', views.get_services_view, name='get_services_view'),
    path('rates/', views.get_rates_view, name='get_rates_view'),
    path('benefits/', views.get_benefits_view, name='get_benefits_view'),
    path('reviews/', views.get_reviews_view, name='get_reviews_view'),
    path('qna/', views.get_qna_view, name='get_qna_view'),
    path('contacts/', views.get_contacts_view, name='get_contacts_view'),
    path('calculator/', views.get_calc_view, name='get_calc_view')
]
