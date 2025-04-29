from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Menu, Booking, Category
from .serializers import MenuSerializer, BookingSerializer, CategorySerializer

def index(request):
    return render(request, "index.html")

def index2(request):
    return render(request, "index2.html")

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer