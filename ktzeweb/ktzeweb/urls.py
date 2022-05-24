from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
