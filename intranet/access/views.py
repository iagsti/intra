from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core import mail
from django.core.paginator import Paginator
from django.conf import settings
from django.template.loader import render_to_string
from django.views.generic.edit import UpdateView
from intranet.access.forms.forms import AccessForm
from intranet.access.models import Access
from intranet.access.filters import AccessFilter
from intranet.access.filters import PERPAGE
from django_filters.views import FilterView
from intranet.core.mixins import PaginatorMixin


def new(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    if request.method == 'POST':
        return create(request)

    return empty_form(request)

def create(request):
    form = AccessForm(request.POST)
    if not form.is_valid():
        return render(request, 'access/access_form.html', {'form': form})

    access = Access.objects.create(**form.cleaned_data)
    request.user.access_set.add(access)

    _send_email({'access': access})
    messages.success(request, 'Solicitação enviada com sucesso.')

    return empty_form(request)

def access_edit(request, slug):
    if request.method == 'POST':
        return _access_update(request, slug)
    access = Access.objects.filter(uuid=slug).values()
    form = AccessForm(access[0])
    return render(request, 'access/access_edit.html', {'form': form})

def detail(request, slug):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    access = Access.objects.get(uuid=slug)
    context = {'access': access}
    return render(request, 'access/access_detail.html', context)
            
def access_list(request):
    paginator = PaginatorMixin(model=Access, filterset=AccessFilter, request=request)
    paginator.set_per_page(PERPAGE)
    pages = paginator.get_paginator()
    context = {'list': pages['object_list'], 'page_list': pages['page_list']}
    return render(pages['request'], 'access/access_list.html', context)

def _access_update(request, slug):
    form = AccessForm(request.POST)
    if not form.is_valid():
        return render(request, 'access/access_edit.html', {'form': form})
    
    access = Access.objects.get(uuid=slug)
    access.period_from = form.cleaned_data['period_from']
    access.period_to = form.cleaned_data['period_to']
    access.time_from = form.cleaned_data['time_from']
    access.time_to = form.cleaned_data['time_to']
    access.status = form.cleaned_data['status']
    access.enable = form.cleaned_data['enable']
    
    access.save()
    return render(request, 'access/access_edit.html', {'form': form})

def empty_form(request):
    return render(request, 'access/access_form.html', {'form': AccessForm()})

def _send_email(context):
    subject = '[IAG-INTRANET] Solicitação de acesso'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = 'intranet@mailinator.com'
    body = render_to_string('email/new_access.txt', context)
    mail.send_mail(subject, body, from_email, [to_email])
