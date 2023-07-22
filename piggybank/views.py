from django.shortcuts import render
from piggybank.models import Currency, Category
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from piggybank.serializers import CurrencySerializer, CategorySerializer

# Create your views here.


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
