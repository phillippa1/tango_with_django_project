from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html
from rango.models import Category
from rango.models import Page




def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    return render(request, 'rango/index.html', context=context_dict)
    # category_list = Category.objects.order_by('-likes')[:5]
    # page_list = Page.objects.order_by('-views')[:5]  # Get the top five most viewed pages
    # context_dict = {}
    # context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    # context_dict['categories'] = category_list
    # context_dict['pages'] = page_list  # Add the top five most viewed pages to the context dictionary

    # # Add the test category to the context dictionary
    # test_category = Category.objects.get(name='Test Category')
    # context_dict['test_category'] = test_category

    # return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'about page context dictionary'}
    context_dict['categories'] = Category.objects.all()
    context_dict['index_url'] = reverse('rango:index')
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        pages = Page.objects.filter(category=category)
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
        return render(request, 'rango/category.html', context=context_dict)
def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)
    
