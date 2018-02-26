# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
# from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from datetime import datetime
import calendar

def index(request):
    context_list_category = Category.objects.order_by('-likes')[:5]
    content_list_page = Page.objects.order_by('-views')[:5]

    # Homepage date display
    now = datetime.now()
    day_iso = now.isocalendar()
    day_name = calendar.day_name[now.weekday()]

    # Orchestrate feedback dictionary to template
    context_dict = {
        'top5_categories': context_list_category,
        'today': now,
        'day_iso_w': day_iso[1],
        'day_name': day_name,
        'top5_pages': content_list_page}
    # return render(request, 'rango/index.html', context_dict)

    # visits = int(request.COOKIES.get('visit', '1')) # set default non-existence to 1  
    # reset_last_visit_time = False
    # response = render(request, 'rango/index.html', context_dict)

    # if 'last_visit' in request.COOKIES:
    #     last_visit = request.COOKIES['last_visit']
    #     last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
    #     if (datetime.now() - last_visit_time).seconds > 1:
    #         visits = visits + 1
    #         reset_last_visit_time = True
    # else:
    #     reset_last_visit_time = True
    #     context_dict['visits'] = visits
    #     response = render(request, 'rango/index.html', context_dict)
    
    # if reset_last_visit_time:
    #     response.set_cookie('last_visit', datetime.now())
    #     response.set_cookie('visits', visits)
    
    visits = request.session.get('visits')
    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_visit_time).seconds > 0:
            visits = visits + 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits
    context_dict['visits'] = visits
    response = render(request, 'rango/index.html', context_dict)

    return response


def about(request):
    context_dict = {
        'aboutmessage': 'Welcome for contact as below.'
    }
    return render(request, 'rango/about.html', context_dict)
    # return HttpResponse("This is about page. <br/> <a href='/rango/'>Index</a>")


def category(request, category_name_slug):
    context_dict = {}
    # try:
    #     c = Category.objects.get(slug=category_name_slug)
    #     context_dict['category_name'] = c.name 
        
    #     pages = Page.objects.filter(category=c)
    #     context_dict['pages'] = pages
    #     context_dict['category'] = c
    # except Category.DoesNotExist:
    #     raise Http404('Category does not exist.')

    c = get_object_or_404(Category, slug=category_name_slug)
    context_dict['category_name'] = c.name 
    
    pages = Page.objects.filter(category=c)
    context_dict['pages'] = pages
    context_dict['category'] = c
    context_dict['category_name_slug'] = c.slug

    return render(request, 'rango/category.html', context_dict)


@login_required
def add_category(request):
    if request.method =='POST':
        forms = CategoryForm(request.POST)
        if forms.is_valid:
            forms.save(commit=True)
            return index(request)
        else:
            print forms.error
    else:
        form = CategoryForm()

    return render(request, 'rango/add_category.html', {'form': form})


@login_required
def add_page(request, category_name_slug):
    cat = get_object_or_404(Category, slug=category_name_slug)

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                # page.views = 0
                page.save()
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {
        'form': form,
        'category_name_slug': cat.slug,
        'category': cat.name
    }
    
    return render(request, 'rango/add_page.html', context_dict)


def register(request):
    #Change to True when registration succeeds.
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # Now we hash the user's password with the set_password method.
            user.set_password(user.password)
            user.save()

            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    context_dict = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }

    return render(request, 'rango/register.html', context_dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponseRedirect('You rango account is disabled.')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse('Invalid login details supplied.')
    else:
        return render(request, 'rango/login.html', {})


@login_required
def restricted(request):
    context_dict={
        'restricted_message': 'Welcome to internal workshop!'
    }
    # return HttpResponse("Since you are logged in, you can see this message!")
    return render(request, 'rango/restricted.html', context_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rango/')

