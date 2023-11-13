from rest_framework import serializers
from instruments.models import Instrument, Order


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ['name', 'description', 'price', 'stock', 'type', 'photo']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['instrument', 'quantity', 'customer_name', 'customer_email', 'order_date']