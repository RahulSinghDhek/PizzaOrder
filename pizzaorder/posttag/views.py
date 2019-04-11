from django.shortcuts import render

from rest_framework import generics
from posttag.models import Tag,Post,PostsTags
from posttag.serializers import TagSerializer , PostSerilaizer


# Create your views here.

class TagViewSet(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostViewSet(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerilaizer
