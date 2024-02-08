from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html
from rango.models import Category
from rango.models import Page
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify




def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    context_dict = {'boldmessage': 'about page context dictionary'}
    context_dict['categories'] = Category.objects.all()
    context_dict['index_url'] = reverse('rango:index')
    return render(request, 'rango/about.html', context=context_dict)

# def show_category(request, category_name_slug):
#     context_dict = {}
#     try:
#         category = Category.objects.get(slug=category_name_slug)
#         context_dict['category_name'] = category.name
#         context_dict['pages'] = Page.objects.filter(category=category)
#     except Category.DoesNotExist:
#         context_dict['category_name'] = None
#         context_dict['pages'] = None
#     return render(request, 'rango/category.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        #context_dict['category_name'] = category.name
        context_dict['pages'] = Page.objects.filter(category=category)
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category_name'] = None
        context_dict['pages'] = None
        context_dict['category'] = None
    return render(request, 'rango/category.html', context=context_dict)
