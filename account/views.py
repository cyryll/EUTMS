from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'account/home.html')

def password(request):
    return render(request,'account/forgotpassword.html')

def signup(request):
    return render(request,'account/register2.html')

def admin(request):
    return render(request,'account/admin.html')

def fleetassistant(request):
    return render(request,'account/fleetassistant.html')

def user(request):
    return render(request,'account/user.html')

def mechanic(request):
    return render(request,'account/mechanic.html')