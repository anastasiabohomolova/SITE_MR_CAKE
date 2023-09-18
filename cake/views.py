from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from cake.models import Info
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from cake.models import Category
from cake.models import Filling


def home_page(request): #домашня сторінка#
    queryset = Category.objects.all()
    context = {
        'title': 'Category',
        'objects_list_kids': queryset.filter(name='Дитячі торти'),
        'objects_list_wedding': queryset.filter(name='Весільні торти'),
        'objects_list_birthday': queryset.filter(name='Торти на день народження'),
        'objects_list_corporate': queryset.filter(name='Корпоративні торти'),
        'objects_list_cake_pops': queryset.filter(name='Кейк-попси'),
        'objects_list_macaroons': queryset.filter(name='Макаруни')
    }
    return render(request, 'home_page.html', context)


def page_kids(request): #сторінка дитячих тортів#
    queryset = Info.objects.filter(type='Дитячі торти')
    query = request.GET.get('q') #пошук товару в даній категорії#
    if query:
        queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(price__icontains=query)
            )
    paginator = Paginator(queryset, 9) #пагінація поділена на 9 елементів#
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1) #повертає на 1 сторінку пагінації, якщо до посилання додається str#
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages) #повертає на останню сторінку пагінції, якщо в посиланні зазначено пагінацію якої немає#

    context = {
        'title': 'Дитячі торти',
        'objects_list': queryset,
        'page_request_var': page_request_var
    }

    return render(request, 'page_cake.html', context)



def page_wedding(request): #сторінка весільних тортів#
    queryset = Info.objects.filter(type="Весільні торти")
    query = request.GET.get('q') #пошук товару в даній категорії#
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query)
        )
    paginator = Paginator(queryset, 9) #пагінація поділена на 9 елементів#
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1) #повертає на 1 сторінку пагінації, якщо до посилання додається str#
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages) #повертає на останню сторінку пагінції, якщо в посиланні зазначено пагінацію якої немає#
    context = {
        'title': 'Весільні торти',
        'objects_list': queryset,
        'page_request_var': page_request_var
    }

    return render(request, 'page_cake.html', context)

def page_birthday(request): #сторінка тортів на день народження#
    queryset = Info.objects.filter(type="Торти на день народження")
    query = request.GET.get('q') #пошук товару в даній категорії#
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query)
        )
    paginator = Paginator(queryset, 9) #пагінація поділена на 9 елементів#
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1) #повертає на 1 сторінку пагінації, якщо до посилання додається str#
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages) #повертає на останню сторінку пагінції, якщо в посиланні зазначено пагінацію якої немає#

    context = {
        'title': 'Торти на день народження',
        'objects_list': queryset,
        'page_request_var': page_request_var
    }

    return render(request, 'page_cake.html', context)

def page_corporate(request): #сторінка корпоративних тортів #
    queryset = Info.objects.filter(type="Корпоративні торти")
    query = request.GET.get('q') #пошук товару в даній категорії#
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query)
        )
    paginator = Paginator(queryset, 9) #пагінація поділена на 9 елементів#
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1) #повертає на 1 сторінку пагінації, якщо до посилання додається str#
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages) #повертає на останню сторінку пагінції, якщо в посиланні зазначено пагінацію якої немає#

    context = {
        'title': 'Корпоративні торти',
        'objects_list': queryset,
        'page_request_var': page_request_var
    }

    return render(request, 'page_cake.html', context)

def page_cake_pops(request): #сторінка #
    queryset = Info.objects.filter(type="Кейк-попси")
    query = request.GET.get('q') #пошук товару в даній категорії#
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query)
        )
    paginator = Paginator(queryset, 9) #пагінація поділена на 9 елементів#
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1) #повертає на 1 сторінку пагінації, якщо до посилання додається str#
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages) #повертає на останню сторінку пагінції, якщо в посиланні зазначено пагінацію якої немає#

    context = {
        'title': 'Cake pops',
        'objects_list': queryset,
        'page_request_var': page_request_var
    }

    return render(request, 'page_cake.html', context)


def page_macaroons(request): #сторінка #
    queryset = Info.objects.filter(type="Макаруни")
    query = request.GET.get('q') #пошук товару в даній категорії#
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query)
        )
    paginator = Paginator(queryset, 9) #пагінація поділена на 9 елементів#
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1) #повертає на 1 сторінку пагінації, якщо до посилання додається str#
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages) #повертає на останню сторінку пагінції, якщо в посиланні зазначено пагінацію якої немає#

    context = {
        'title': 'Macaroons',
        'objects_list': queryset,
        'page_request_var': page_request_var
    }

    return render(request, 'page_cake.html', context)



def page_details(request, id=None): #сторінка детальної інформації товару#
    instance = get_object_or_404(Info, id=id)
    context = {
        'title': 'Detail',
        'object': instance,
    }

    return render(request, 'details_page.html', context)



def page_filling(request): #сторінка про начинки#
    queryset = Filling.objects.all()
    context = {
        'title': 'Fillings',
        'objects_list_cake': queryset.filter(type='Торти/Поп-кейки'),
        'objects_list_macaroons': queryset.filter(type='Макаруни')
    }

    return render(request, 'page_filling.html', context)


def page_order(request): #сторінка про замовлення#
    return render(request, 'page_order.html')



def page_company(request): #сторінка про компанію#
    return render(request, 'page_company.html')







