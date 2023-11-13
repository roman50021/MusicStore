from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema

from .models import Instrument, Order
from .serializers import InstrumentSerializer, OrderSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi


class InstrumentList(APIView):

    @swagger_auto_schema(
        operation_description="Get a list of  instruments",
        responses={200: openapi.Response('List of  instruments', InstrumentSerializer(many=True))}
    )
    def get(self, request, format=None):
        instrument =  Instrument.objects.all()
        serializer = InstrumentSerializer(instrument, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new instrument",
        request_body=InstrumentSerializer,
        responses={201: 'Created', 400: 'Bad Request'}
    )

    def post(self, request, format=None):
        serializer = InstrumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class  InstrumentDetail(APIView):

    def get_object(self, pk):
        try:
            return Instrument.objects.get(pk=pk)
        except Instrument.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Get details of a specific instrument",
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="Instrument ID", type=openapi.TYPE_INTEGER),
        ],
        responses={200: openapi.Response('Instrument details', InstrumentSerializer)}
    )

    def get(self, request, pk, format=None):
        instrument = self.get_object(pk)
        serializer = InstrumentSerializer(instrument)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update details of a specific instrument",
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="Instrument ID", type=openapi.TYPE_INTEGER),
        ],
        request_body=InstrumentSerializer,
        responses={200: 'Updated', 400: 'Bad Request'}
    )

    def put(self, request, pk, format=None):
        instrument = self.get_object(pk)
        serializer = InstrumentSerializer(instrument, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a specific instrument",
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="Instrument ID", type=openapi.TYPE_INTEGER),
        ],
        responses={204: 'No Content'}
    )
    def delete(self, request, pk, format=None):
        instrument = self.get_object(pk)
        instrument.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderList(APIView):

    @swagger_auto_schema(
        operation_description="Get a list of orders",
        responses={200: openapi.Response('List of orders', OrderSerializer(many=True))}
    )

    def get(self, request, format=None):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new order",
        request_body=OrderSerializer,
        responses={201: 'Created', 400: 'Bad Request'}
    )

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Get details of a specific order",
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="Order ID", type=openapi.TYPE_INTEGER),
        ],
        responses={200: openapi.Response('Order details', OrderSerializer)}
    )

    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update details of a specific order",
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="Order ID", type=openapi.TYPE_INTEGER),
        ],
        request_body=OrderSerializer,
        responses={200: 'Updated', 400: 'Bad Request'}

    )

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a specific order",
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="Order ID", type=openapi.TYPE_INTEGER),
        ],
        responses={204: 'No Content'}
    )

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)