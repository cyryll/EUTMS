from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from .forms import UserLoginForm

# Create your views here.
def login(request,*args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request,user_obj)
        return HttpResponseRedirect("/")
    return render(request,"account/login.html",{"form":form})  

def loggedin(request):
    return render_to_response('login/loggedin.html',
    {'full_name': request.user.staffId})

def invalid_login(request):
    return render_to_response('login/invalid_login.html')


def password(request):
    return render(request,'account/forgotpassword.html')

def signup(request):
    return render(request,'account/register.html')

def admin(request):
    return render(request,'account/admin.html')

def fleetassistant(request):
    return render(request,'account/fleetassistant.html')

def user(request):
    return render(request,'account/user.html')

def mechanic(request):
    return render(request,'account/mechanic.html')