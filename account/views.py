from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, get_user_model, authenticate
from .forms import UserLoginForm, UserCreationForm
from management.forms import VehiclesForm, RequestForm

# Create your views here.


def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect("{% url 'login' %}")
    context = {'form': form}
    return render(request, 'account/register.html', context)


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


def password(request):
    return render(request, 'account/forgotpassword.html')


def admin(request):
    if request.POST:
        form = VehiclesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("{% url 'admin' %}")
    else:
        form = VehiclesForm()
    return render(request, 'account/admin.html', {"form": form})


def fleetassistant(request):
    return render(request, 'account/fleetassistant.html')


def user(request):
    if request.POST:
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("{% url 'user' %}")
    else:
        form = RequestForm()
    return render(request, 'account/user.html', {"form": form})


def mechanic(request):
    return render(request, 'account/mechanic.html')


def requests(request):
    return render(request, 'account/requests.html')


def booking_status(request):
    return render(request, 'account/booking_status.html')


def add_driver(request):
    return render(request, 'account/add_driver.html')


def remove_driver(request):
    return render(request, 'account/remove_driver.html')


def add_vehicle(request):
    return render(request, 'account/user.html')


def remove_vehicle(request):
    return render(request, 'account/remove_vehicle.html')


def user_details(request):
    return render(request, 'account/user_details.html')


def mechanics(request):
    return render(request, 'account/add_mechanic.html')


def add_sparepart(request):
    return render(request, 'account/add_spareparts.html')
