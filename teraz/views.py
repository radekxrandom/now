from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth import authenticate
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Info, GetPies, MainCMS, PrzedCMS, PoCMS, GetInfoCMS
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/login')
def main_page(request):
    template_name = 'main.html'
    cms = MainCMS.objects.all()
    context = {'cms': cms}
    if request.method == 'GET':
        return render(request, template_name, context)
    if request.method == 'POST':
        line_num = request.POST.get('numline')
        line_pl = request.POST.get('plline')
        main = MainCMS.objects.get(pk=line_num)
        main.line_pl = line_pl
        main.save()
        return render(request, template_name, context)

def get_info(request):
    template_name = 'get_info.html'
    if request.method == 'GET':
        cms = GetInfoCMS.objects.all()
        context = {'cms': cms}
        return render(request, template_name, context)
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


@login_required(login_url='/login')
def przed(request):
    template_name = 'przed.html'
    cms = PrzedCMS.objects.all()
    context = {'cms': cms}
    if request.method == 'GET':
        return render(request, template_name, context)
    if request.method == 'POST':
        line_num = request.POST.get('numline')
        line_pl = request.POST.get('plline')
        przed = PrzedCMS.objects.get(pk=line_num)
        przed.line_pl = line_pl
        przed.save()
        return render(request, template_name, context)

@login_required(login_url='/login')
def teraz(request):
    template_name = 'teraz.html'
    return render(request, template_name)

@login_required(login_url='/login')
def po(request):
    template_name = 'po.html'
    cms = PoCMS.objects.all()
    context = {'cms': cms}
    if request.method == 'GET':
        return render(request, template_name, context)
    if request.method == 'POST':
        line_num = request.POST.get('numline')
        line_pl = request.POST.get('plline')
        po = PoCMS.objects.get(pk=line_num)
        po.line_pl = line_pl
        po.save()
        return render(request, template_name, context)

def login(request):
    template_name = 'login.html'
    if request.method == 'POST':
        username = request.POST['password']
        password = 'useruser'
        user = authenticate(request, username=username, password=password)
        if user is not None:
            from django.contrib.auth import login
            request.session.set_expiry(259200)
            login(request, user)
            u = User.objects.get(username = username)
            u.username = 'ugh'
            u.save
            return HttpResponseRedirect(reverse('teraz:main_page'))
        else:
            return HttpResponseRedirect(reverse('teraz:login'))
    else:
        return render(request, template_name)

@user_passes_test(lambda u: u.is_superuser)
def block(request):
    return redirect('main_page')


@user_passes_test(lambda u: u.is_superuser)
def CMS(request):
    template_name = 'cms.html'
    if request.method == 'GET':
        main = MainCMS.objects.all()
        przed = PrzedCMS.objects.all()
        po = PoCMS.objects.all()
        get  = GetInfoCMS.objects.all()
        context = {'main': main, 'przed': przed, 'po': po, 'get': get}
        return render(request, template_name, context)
    if request.method == 'POST':
        if 'edit_main' in request.POST:
            line_num = request.POST.get('numline')
            line_eng = request.POST.get('engline')
            line_pl = request.POST.get('plline')
            try:
                main = MainCMS.objects.get(pk=line_num)
                main.line_eng = line_eng
                main.line_pl = line_pl
                main.save()
            except MainCMS.DoesNotExist:
                main = MainCMS(line_eng=line_eng, line_pl=line_pl)
                main.save()
            main = MainCMS.objects.all()
            przed = PrzedCMS.objects.all()
            po = PoCMS.objects.all()
            get  = GetInfoCMS.objects.all()
            context = {'main': main, 'przed': przed, 'po': po, 'get': get}
            return render(request, template_name, context)
        if 'edit_przed' in request.POST:
            line_num = request.POST.get('numline')
            line_eng = request.POST.get('engline')
            line_pl = request.POST.get('plline')
            try:
                przed = PrzedCMS.objects.get(pk=line_num)
                przed.line_eng = line_eng
                przed.line_pl = line_pl
                przed.save()
            except PrzedCMS.DoesNotExist:
                przed = PrzedCMS(line_eng=line_eng, line_pl=line_pl)
                przed.save()
            main = MainCMS.objects.all()
            przed = PrzedCMS.objects.all()
            po = PoCMS.objects.all()
            get  = GetInfoCMS.objects.all()
            context = {'main': main, 'przed': przed, 'po': po, 'get': get}
            return render(request, template_name, context)
        if 'edit_po' in request.POST:
            line_num = request.POST.get('numline')
            line_eng = request.POST.get('engline')
            line_pl = request.POST.get('plline')
            try:
                po = PoCMS.objects.get(pk=line_num)
                po.line_eng = line_eng
                po.line_pl = line_pl
                po.save()
            except PoCMS.DoesNotExist:
                po = PoCMS(line_eng=line_eng, line_pl=line_pl)
                po.save()
            main = MainCMS.objects.all()
            przed = PrzedCMS.objects.all()
            po = PoCMS.objects.all()
            get  = GetInfoCMS.objects.all()
            context = {'main': main, 'przed': przed, 'po': po, 'get': get}
            return render(request, template_name, context)
        if 'edit_getinfo' in request.POST:
            line_num = request.POST.get('numline')
            line_eng = request.POST.get('engline')
            line_pl = request.POST.get('plline')
            try:
                get = GetInfoCMS.objects.get(pk=line_num)
                get.line_eng = line_eng
                get.line_pl = line_pl
                get.save()
            except GetInfoCMS.DoesNotExist:
                get = GetInfoCMS(line_eng=line_eng, line_pl=line_pl)
                get.save()
            main = MainCMS.objects.all()
            przed = PrzedCMS.objects.all()
            po = PoCMS.objects.all()
            get  = GetInfoCMS.objects.all()
            context = {'main': main, 'przed': przed, 'po': po, 'get': get}
            return render(request, template_name, context)
