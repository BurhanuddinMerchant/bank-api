from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.serializers import Serializer
from .serializers import BankSerializer
from .models import Bank


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankFilteredAutocompleteView(generics.ListAPIView):
    serializer_class = BankSerializer

    def get_queryset(self):
        query = self.request.query_params.get("q")
        limit = self.request.query_params.get("limit")
        offset = self.request.query_params.get("offset")
        if limit is not None and offset is not None:
            queryset = (
                Bank.objects.all()
                .filter(branch__istartswith=query)
                .order_by("ifsc")[int(offset) : int(offset) + int(limit)]
            )
            return queryset
        else:
            queryset = (
                Bank.objects.all().filter(branch__istartswith=query).order_by("ifsc")
            )
            return queryset


class BankFilteredSearchView(generics.ListAPIView):
    serializer_class = BankSerializer

    def get_queryset(self):
        query = self.request.query_params.get("q")
        limit = self.request.query_params.get("limit")
        offset = self.request.query_params.get("offset")
        if limit is not None and offset is not None:
            queryset = (
                Bank.objects.all()
                .filter(city=query)
                .order_by("ifsc")[int(offset) : int(offset) + int(limit)]
            )
            return queryset
        else:
            queryset = Bank.objects.all().filter(city=query).order_by("ifsc")
            return queryset
