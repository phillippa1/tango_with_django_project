from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html
from rango.models import Category




def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in our context_dict dictionary (with our boldmessage!)
    # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    #index_url = reverse('index')
    #index_link = format_html('<a href="{}">index</a>', index_url)
    #response = f'Rango says here is the about page. {index_link}'
    #return HttpResponse(response)
    context_dict = {'boldmessage': 'about page context dictionary'}
    context_dict['categories'] = Category.objects.all()
    context_dict['index_url'] = reverse('rango:index')
    return render(request, 'rango/about.html', context=context_dict)
    
