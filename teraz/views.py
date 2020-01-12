from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth import authenticate
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.contrib import messages 
from .models import Info, GetPies
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.
#@login_required
def main_page(request):
    template_name = 'main.html'
    return render(request, template_name)

def get_info(request):
    template_name = 'get_info.html'
    if request.method == 'GET':
        return render(request, template_name)
    elif request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        reason = request.POST['reason']
        pach = GetPies.objects.create(name=name, mail=mail, reason=reason)
        message = Mail(
            from_email='from_email@example.com',
            to_emails='jozwa.zawadiaka@gmail.com,jaceklaaser1@gmail.com',
            subject='New acces code request',
            html_content='Name: {name}, mail: {mail}, wybrany utwor: {reason}')
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
        return HttpResponseRedirect(reverse('teraz:login'))


#@login_required
def przed(request):
    template_name = 'przed.html'
    return render(request, template_name)

#@login_required
def teraz(request):
    template_name = 'teraz.html'
    return render(request, template_name)

#@login_required
def po(request):
    template_name = 'po.html'
    return render(request, template_name)

def login(request):
    template_name = 'login.html'
    if request.method == 'POST':
        password = request.POST['password']
        username = 'user'
        user = authenticate(request, username=username, password=password)
        if user is not None:
            from django.contrib.auth import login
            login(request, user)
            return HttpResponseRedirect(reverse('teraz:main'))
        else:
            return HttpResponseRedirect(reverse('teraz:login'))
    else:
        return render(request, template_name)

