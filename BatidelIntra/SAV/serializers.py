from django.shortcuts import get_object_or_404
from rest_framework import serializers

from customers.models import Customer
from .models import SAV


class SAVCustomerSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        return get_object_or_404(Customer, pk=data['id'])

    class Meta:
        model = Customer
        fields = (
            'id', 'firstName', 'lastName', 'address', 'city', 'phone', 'port'
        )


class SAVSerializer(serializers.ModelSerializer):
    customer_name = serializers.ReadOnlyField(source='customer.lastName')
    customer = SAVCustomerSerializer()
    customer_view = SAVCustomerSerializer(source="customer", read_only=True)
    class Meta:
        model = SAV
        fields = (
            'id',
            'creationDate',
            'customer_name',
            'state',
            'nature',
            'furnitureReception',
            'programmation',
            'conclusion',
            'customer',
            'customer_view'
        )