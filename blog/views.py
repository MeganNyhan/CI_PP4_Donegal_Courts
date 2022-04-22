# imports
from django.views.generic import ListView, DetailView, CreateView
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


class AddPostView(CreateView):
    """
        Create Add post view for creating blog posts on the site
    """
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'
