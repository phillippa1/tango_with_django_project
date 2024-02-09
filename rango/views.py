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
from rango.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



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
@login_required
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

@login_required
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



def register(request):
  registered = False
  if request.method == 'POST':
    user_form = UserForm(request.POST)
    profile_form = UserProfileForm(request.POST)

    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save()
      user.set_password(user.password)
      user.save()
      profile = profile_form.save(commit=False)
      profile.user = user

      if 'picture' in request.FILES:
        profile.picture = request.FILES['picture']

      profile.save()
      registered = True
    else:
      print(user_form.errors, profile_form.errors)
  else:
    user_form = UserForm()
    profile_form = UserProfileForm()

  return render(request,
                'rango/register.html',
                context = {'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def user_login(request):
  if request.method == 'POST':
    # Gather the username and password provided by the user.
    username = request.POST.get('username')
    password = request.POST.get('password')

    # Use Django's machinery to attempt to see if the username/password
    # combination is valid - a User object is returned if it is.
    user = authenticate(username=username, password=password)

    # If we have a User object, the details are correct.
    if user:
      # Is the account active? It could have been disabled.
      if user.is_active:
        # If the account is valid and active, we can log the user in.
        # We'll send the user back to the homepage.
        login(request, user)
        return redirect(reverse('rango:index'))
      else:
        # An inactive account was used - no logging in!
        return HttpResponse("Your Rango account is disabled.")
    else:
      # Bad login details were provided. So we can't log the user in.
      print(f"Invalid login details: {username}, {password}")
      return HttpResponse("Invalid login details supplied.")
  else:
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    return render(request, 'rango/login.html')
  
@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

# Use the login_required() decorator to ensure only those logged in can
# access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('rango:index'))



@login_required
def restricted(request):
  return render(request, 'rango/restricted.html')


