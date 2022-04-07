from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
        This view will render the list of posts on the blog.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

# Create your views here.
