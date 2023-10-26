from django.shortcuts import render
from rest_framework import generics, viewsets
from restaurant.serializers import MenuSerializer,BookingSerializer
from .models import MenuItem
from rest_framework.permissions import IsAuthenticated


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()  
    serializer_class = MenuSerializer  

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()  
    serializer_class = MenuSerializer