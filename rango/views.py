from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html
from rango.models import Category
from rango.models import Page
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from rango.forms import CategoryForm
from django.shortcuts import redirect
from rango.forms import PageForm





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

def add_category(request):
    form = CategoryForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
    # Have we been provided with a valid form?
    if form.is_valid():
        # Save the new category to the database.
        form.save(commit=True)
        # Now that the category is saved, we could confirm this.
        # For now, just redirect the user back to the index view.
        return redirect('/rango/')
    else:
    # The supplied form contained errors -
        # just print them to the terminal.
        print(form.errors)
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    # You cannot add a page to a Category that does not exist...
    if category is None:
        return redirect('/rango/')
    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return redirect(reverse('rango:show_category',
                                        kwargs={'category_name_slug': category_name_slug}))
            else:
                print(form.errors)
                context_dict = {'form': form, 'category': category}
                return render(request, 'rango/add_page.html', context=context_dict)
