from django.urls import path
from .views import *

urlpatterns = [
    # path('home/',HomeView.as_view(),name='home'),
    path('about/',AboutView.as_view(),name='about'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('post/',PostView.as_view(),name='post'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    path('skill/',SkillView.as_view(),name='skill'),
    path('service/',ServiceView.as_view(),name='service'),
    path('resume/',ResumeView.as_view(),name='resume'),
    path('myblog/',MyBlogView.as_view(),name='myblog'),
]