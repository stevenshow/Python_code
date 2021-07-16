from rest_framework import serializers
from .models import Dates

class DatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dates
        fields = ('id', 'event_Name', 'event_Date')