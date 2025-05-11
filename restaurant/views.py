from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Menu, Booking, Category
from .serializers import MenuSerializer, BookingSerializer, CategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


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


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

