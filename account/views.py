from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, get_user_model,authenticate
from .forms import UserLoginForm, UserCreationForm


# Create your views here.


def register(request,*args, **kwargs):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect("")
    context = {
        'form':form
    }
    return render(request,'account/register.html' ,context)
def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return HttpResponseRedirect("administration/")
    return render(request, "account/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login")


def password(request):
    return render(request, 'account/forgotpassword.html')


def signup(request):
    return render(request, 'account/register.html')


def admin(request):
    return render(request, 'account/admin.html')


def fleetassistant(request):
    return render(request, 'account/fleetassistant.html')


def user(request):
    return render(request, 'account/user.html')


def mechanic(request):
    return render(request, 'account/mechanic.html')
