from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import MenuSerializer,BookingSerializer
from .models import Menu, Booking



class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()  
    serializer_class = MenuSerializer  

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()  
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    

