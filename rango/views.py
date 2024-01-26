from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html



def index(request):
    about_url = reverse('about')
    about_link = format_html('<a href="{}">about</a>', about_url)
    response = f'Rango says hey there partner! {about_link}'
    return HttpResponse(response)

def about(request):
    index_url = reverse('index')
    index_link = format_html('<a href="{}">index</a>', index_url)
    response = f'Rango says here is the about page. {index_link}'
    return HttpResponse(response)
    
