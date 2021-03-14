from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, get_user_model, authenticate
from .forms import UserLoginForm, UserCreationForm



# Create your views here.

def register(request,*args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context = {
        'form':form
    }
    return render(request,'account/register.html' ,context)


def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return HttpResponseRedirect("user/")
    return render(request, "account/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")