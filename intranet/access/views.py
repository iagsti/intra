from django.shortcuts import render, redirect
from django.contrib import messages
from django.core import mail
from django.conf import settings
from django.template.loader import render_to_string
from intranet.access.forms.forms import AccessForm
from intranet.access.models import Access


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
    _send_email({'access': access})
    messages.success(request, 'Solicitação enviada com sucesso.')

    return empty_form(request)


def empty_form(request):
    return render(request, 'access/access_form.html', {'form': AccessForm()})


def _send_email(context):
    subject = '[IAG-INTRANET] Solicitação de acesso'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = 'intranet@mailinator.com'
    body = render_to_string('email/new_access.txt', context)
    mail.send_mail(subject, body, from_email, [to_email])
