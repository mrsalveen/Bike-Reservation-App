
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from .models import Reservation
from django.urls import reverse_lazy

from audioop import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from bike_app.models import Complaint, BikeInfo
from django.contrib import messages
import tkinter.messagebox
from tkinter import *



# Create your views here.

def home(request):
    return render(request, 'home.html')

def Welcome_page(request):
    #find it on templates DIR of app DIR
    return render(request, "welcome.html")


def FeedBack_page(request):
    return render(request, "complaint.html")




def add_complaint(request):
    if request.method == 'POST':
        new_Complaint_id = request.POST.get("complaint_id")
        new_Complaint_Descriptions = request.POST.get('Descriptions')#complaint_id=new_Complaint_id
        Complaint.objects.create(complaint_id=new_Complaint_id,Descriptions=new_Complaint_Descriptions) 
        return redirect('../')  
    return render(request, "complaint.html")

def bikeList_page(request):
    bike = BikeInfo.objects.all()
    return render(request, "bikeList.html", {"bike_list": bike})

# def bike_list(request):
#    return render(request, 'bike_list.html')

def bike_info1(request):
   bike = BikeInfo.objects.all().filter(BikeName="KROSS LEVEL BOOST 2.0 2021")
   return render(request, 'bikeInfo.html',{"bike_info": bike})

def bike_info2(request):
   bike = BikeInfo.objects.all().filter(BikeName="KROSS LEA BOOST 3.0 2021")
   return render(request, 'bikeInfo.html',{"bike_info": bike})

def bike_info3(request):
   bike = BikeInfo.objects.all().filter(BikeName="GIANT FATHOM E+ JUNIOR 2021")
   return render(request, 'bikeInfo.html',{"bike_info": bike})

def bike_info4(request):
   bike = BikeInfo.objects.all().filter(BikeName="ROAD BIKE 3.0 2021")
   return render(request, 'bikeInfo.html',{"bike_info": bike})

def bike_info5(request):
   bike = BikeInfo.objects.all().filter(BikeName="ROAD BIKE BOOST 2.0 2020")
   return render(request, 'bikeInfo.html',{"bike_info": bike})

def bike_info6(request):
   bike = BikeInfo.objects.all().filter(BikeName="ROAD BIKE 3.1 2021")
   return render(request, 'bikeInfo.html',{"bike_info": bike})

def recharge(request):
    return render(request,'recharge.html')

def FAQ(request):
    return  render(request,'FAQ.html')


# class Reservation_Page(CreateView):
#     model = Reservation
#     fields = '__all__'
#     success_url = reverse_lazy('home')
#     template_name = 'bike_app/reservation.html'


class ReservationCreate(CreateView):
    model = Reservation
    fields = '__all__'
    success_url = reverse_lazy('bike_app:reservations')
    #template_name = 'bike_app/reservation.html'

class ReservationPage(DetailView):
    model = Reservation
    context_object_name = 'reservation'

class ReservationList(ListView): 
    model = Reservation
    context_object_name = 'reservations'

class ReservationUpdate(UpdateView):
    model = Reservation
    fields = '__all__'
    success_url = reverse_lazy('bike_app:reservations')
    #template_name = 'edit_reservation.hthml'

class ReservationDelete(DeleteView):
    model=Reservation
    context_object_name='reservation'
    success_url=reverse_lazy('bike_app:reservations')

