from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


from .models import Employee, checkin, checkout
from .forms import signupForm, loginForm, checkinoutForm

import datetime, itertools
# Create your views here

def index(request):
    return render(request, 'swipe/index.html',{})

def user_login(request):
    l_form = loginForm(request.POST or None)
    text = "Login"
    pwd_flag = False#set true if wrong passsword entered
    alert_text = ""
    if request.method == 'POST':
        if l_form.is_valid():
            usr = l_form.clean_username()
            pwd = l_form.clean_password()
            user_to_login = authenticate(username = usr, password = pwd)
            if user_to_login is not None:
                login(request, user_to_login)
                return redirect('user_home_page', name = usr)
            else:
                pwd_flag =True
                alert_text = "Please enter correct credentials"
    context = {
        'form': l_form,
        'note': text,
        'alert': alert_text
    }

    return render(request, 'swipe/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('user_login')

def signup(request):
    reg_form = signupForm(request.POST or None)
    text = "Register Here"
    if request.method == 'POST':
        if reg_form.is_valid():
            #reg_form.save(commit = False)
            usrnm = reg_form.cleaned_data.get('username')
            pwd1 = reg_form.cleaned_data.get('password1')
            mail = reg_form.cleaned_data.get('email')
            User.objects.create_user(username = usrnm, password = pwd1, email = mail)
            user_to_login = authenticate(username = usrnm, password = pwd1)
            if user_to_login is not None:
                login(request, user_to_login)
                return redirect('user_home_page', username = usrnm)

    context = {
        'form':reg_form,
        'note':text
    }

    return render(request, 'swipe/register.html', context)

def user_home(request, name):
    if request.user.is_authenticated and request.user.username == name:
        welcome_note = "Welcome " + str(name)
        c_form = checkinoutForm(request.POST or None)
        employee_obj = Employee.objects.get(user = User.objects.get(username = name))
        u_name = employee_obj.user.username
        mail = employee_obj.user.email
        start_time = (datetime.datetime.now() - datetime.timedelta(days = 1)).replace(hour = 0, minute = 0, second = 0, microsecond = 0)
        L_checkout = checkout.objects.filter(creator = employee_obj, time__gte = start_time).order_by("-time")[0]
        L_checkin = checkin.objects.filter(creator = employee_obj, time__gte = start_time).order_by("time")[0]

        if request.method == 'POST':
            if request.POST['Check_Select'] == 'in':
                checkin.objects.create(creator = employee_obj)
            else:
                checkout.objects.create(creator = employee_obj)

        context = {'form':c_form,'u_name':u_name,'email':mail,'note':welcome_note,'l_in':L_checkin,'l_out':L_checkout}
        return render(request, 'swipe/user_home.html', context)
    else:
        return redirect(user_login)

def user_history(request, name):
    if request.user.is_authenticated and request.user.username == name:
        employee_obj = Employee.objects.get(user = User.objects.get(username = name))
        checkins = list(checkin.objects.filter(creator = employee_obj).order_by("-time"))
        checkouts = list(checkout.objects.filter(creator = employee_obj).order_by("-time"))
        ch = itertools.zip_longest(checkins, checkouts, fillvalue = "")
        context = {
            'emp_obj':employee_obj,
            'ch':ch
        }

        return render(request, 'swipe/history.html', context)
    else:
        return redirect(user_login)
