from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .serializers import (
    ComplaintSerializer,
    SearcheeSerializer,
    SearcheeSampleSerializer,
    SearchSerializer,
    SearchResultSerializer
)
from .models import Complaint, Searchee, SearcheeSample, Search, SearchResult


class ComplaintViewSet(viewsets.ModelViewSet):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()


class SearcheeViewSet(viewsets.ModelViewSet):
    serializer_class = SearcheeSerializer
    queryset = Searchee.objects.all()


class SearcheeSampleViewSet(viewsets.ModelViewSet):
    serializer_class = SearcheeSampleSerializer
    queryset = SearcheeSample.objects.all()


class SearchViewSet(viewsets.ModelViewSet):
    serializer_class = SearchSerializer
    queryset = Search.objects.all()


class SearchResultViewSet(viewsets.ModelViewSet):
    serializer_class = SearchResultSerializer
    queryset = SearchResult.objects.all()
