# imports
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class HomeView(ListView):
    """
        Create view for blog post list in home page
    """
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    """
        Create view for blog post details in post detail page
    """
    model = Post
    template_name = 'post_detail.html'
