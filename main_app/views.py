from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

# class HomeView(generics.ListAPIView):
#     queryset = HomeSerializer
#     serializer_class = HomeSerializer

class PostView(generics.ListCreateAPIView):
    queryset = PostSerializer
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostSerializer
    serializer_class = PostSerializer

class ContactView(generics.ListAPIView):
    queryset = ContactSerializer
    serializer_class = ContactSerializer

class AboutView(generics.ListAPIView):
    queryset = AboutSerializer
    serializer_class = AboutSerializer