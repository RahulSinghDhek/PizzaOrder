from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from rest_framework import generics
from pizzaorder.test_MM.models import PersonCase,Person,Case
from pizzaorder.test_MM.serializers import PersonSerializer, CaseSerializer, PersonCasetSerializer


# Create your views here.

class PersonViewset(generics.ListCreateAPIView):
    queryset = PersonCase.objects.all()
    serializer_class = PersonSerializer

class CaseViewSet(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer