from django.shortcuts import render


def get_home_view(request):
    return render(request, 'home/home.html')

def get_documents_view(request):
    return render(request, 'home/documents.html')

def get_services_view(request):
    return render(request, 'home/services.html')

def get_rates_view(request):
    return render(request, 'home/rates.html')

def get_benefits_view(request):
    return render(request, 'home/benefits.html')

def get_reviews_view(request):
    return render(request, 'home/reviews.html')

def get_qna_view(request):
    return render(request, 'home/qna.html')

def get_contacts_view(request):
    return render(request, 'home/contacts.html')

def get_calc_view(request):
    return render(request, 'home/calculator.html')
