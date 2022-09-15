from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

# Create your views here.
class RoomView(generics.ListAPIView):
    queryset= Room.objects.all()
    fields = '__all__'
    serializer_class = RoomSerializer

