from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

# class HomeView(generics.ListAPIView):
#     queryset = HomeSerializer
#     serializer_class = HomeSerializer

class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ContactView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class SkillView(generics.ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer

class ServiceView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

class ResumeView(generics.ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class MyBlogView(generics.ListAPIView):
    queryset = MyBlog.objects.all()
    serializer_class = MyBlogSerializer
