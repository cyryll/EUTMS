from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import VehiclesForm, RequestForm, SparePartForm, DriverForm, MechanicForm
from .models import Vehicle, Request, SparePart, Driver, Mechanic
from account.models import Users


def admin(request):
    data = Vehicle.objects.all()
    data1 = Driver.objects.all()
    data2 = Users.objects.all()
    if request.POST:
        form = VehiclesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("{% url 'admin' %}")
    else:
        form = VehiclesForm()
    return render(request, 'account/admin.html', {"form": form, "data": data, "data1":data1, "data2":data2})


def mechanics(request):
    if request.POST:
        form = MechanicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("{% url 'mechanic2' %}")
    else:
        form = MechanicForm()
    return render(request, 'account/add_mechanic.html', {"form": form})


def fleetassistant(request):
    data = Request.objects.all()
    data1 = Vehicle.objects.all()
    data2 = Driver.objects.all()
    return render(request, 'account/fleetassistant.html',{'data': data,'data1': data1 , 'data2': data2})


def user(request):
    if request.POST:
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect("{% url 'user' %}")
    else:
        form = RequestForm()
    return render(request, 'account/user.html', {"form": form})


def mechanic(request):
    data = SparePart.objects.all()
    data1 = Mechanic.objects.all()
    if request.POST:
        form = SparePartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("{% url 'mechanic' %}")
    else:
        form = SparePartForm()
    return render(request, 'account/mechanic.html', {"form": form, "data": data, "data1":data1})


def requests(request):
    return render(request, 'account/requests.html')


def booking_status(request):
    return render(request, 'account/booking_status.html')


def fleetview(request):
    data = Request.objects.all()
    data1 = Vehicle.objects.all()
    data2 = Driver.objects.all()
    return render(request, 'account/fleetview.html', {'data': data , 'data1': data1 , 'data2': data2})


def remove_driver(request):
    if request.POST:
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            print("Added Driver")
            return HttpResponseRedirect("{% url 'admin' %}")
    else:
        print("Did not add driver")
        form = DriverForm(request.POST)
        return render(request, 'account/remove_driver.html', {"form": form})


def add_vehicle(request):
    return render(request, 'account/user.html')


def remove_vehicle(request):
    return render(request, 'account/remove_vehicle.html')


def admin2(request):
    return render(request, 'account/admin.html')


def mechanic2(request):
    return render(request, 'account/mechanic.html')


def add_sparepart(request):
    return render(request, 'account/add_spareparts.html')
