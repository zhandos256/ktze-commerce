from django.shortcuts import render


def get_blog_view(request):
    return render(request, 'blog/home.html')
