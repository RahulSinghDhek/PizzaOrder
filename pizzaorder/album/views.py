from album.models import Album,Track
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from album.serializers import TrackSerializer,AlbumSerializer

class AlbumViewSet(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class TrackViewSet(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


