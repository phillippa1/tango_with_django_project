from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html



def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    #index_url = reverse('index')
    #index_link = format_html('<a href="{}">index</a>', index_url)
    #response = f'Rango says here is the about page. {index_link}'
    #return HttpResponse(response)
    context_dict = {'boldmessage': 'about page context dictionary'}
    return render(request, 'rango/about.html', context=context_dict)
    
