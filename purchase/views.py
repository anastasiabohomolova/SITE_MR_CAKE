from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from purchase.models import Purchase
from purchase.forms import PurchaseForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from cake.models import Info



def create_order(request): #створення замовлення по формочці#
    form = PurchaseForm(request.POST or None,
                       request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, f'<a href="/mr_cake/" style="color: black;">Перейти на головну</a> Заявка на замовлення оформленна!', extra_tags='html_safe') #повертає повідомлення після оформення замовлення, яке має посилання на головну сторінку#
        return HttpResponseRedirect(instance.page_purchase()) #відпралення замовлення повертає на сторінку purchase#
    context = {
        'title': 'Create order',
        'form': form
    }
    return render(request, 'create_order.html', context)



