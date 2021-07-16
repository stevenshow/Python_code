from django.shortcuts import render
from rest_framework import generics
from .serializers import DatesSerializer
from .models import Dates

# Create your views here.

# Allows viewing and adding dates
class DateView(generics.ListAPIView):
    queryset = Dates.objects.all()
    serializer_class = DatesSerializer

class DateAdd(generics.CreateAPIView):
    queryset = Dates.objects.all()
    serializer_class = DatesSerializer