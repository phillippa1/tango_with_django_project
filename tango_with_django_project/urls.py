"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from rango import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('rango/', include('rango.urls', namespace='rango')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('rango/about/', views.about, name='about'),
    # path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    #path('about/', views.about, name='about'),
    #path('', include('rango.urls')),
    
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 #path('', views.about, name='about'),
    #path('rango/about/', views.about, name='about'),
    
    #path('admin/about', admin.site.urls),
    # The above maps any URLs starting with rango/ to be handled by rango.
    #path('', views.index, name='index'),
    #path('admin/index', admin.site.urls),
    #path('', views.about, name='about'),
    #path('', views.index, name='index'),
    #path('rango/', include([
    #    path('about/', views.about, name='about'),
    #])),

