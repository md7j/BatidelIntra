from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = (
            'id', 'firstName', 'lastName', 'address', 'city', 'phone', 'port'
        )
