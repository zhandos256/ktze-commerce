from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article


def get_home_view(request):
    return render(request, 'blog/home.html')

def get_blog_view(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'page_obj': page_obj})

def get_services_view(request):
    return render(request, 'blog/services.html')

def get_documents_view(request):
    return render(request, 'blog/documents.html')

def get_contacts_view(request):
    return render(request, 'blog/contacts.html')

def get_us_view(request):
    return render(request, 'blog/us.html')

def get_request_view(request):
    return render(request, 'blog/request.html')

def get_faq_view(request):
    return render(request, 'blog/faq.html')