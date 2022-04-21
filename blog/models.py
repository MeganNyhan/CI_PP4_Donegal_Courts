"""
imports from Django.
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# This tuple will keep track of drafted posts and published posts
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    This post model will allow me to post onto the
    site, using the required variables.
    """
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_post")
    body = models.TextField()

    def __str__(self):
        return self.title + '|' + self.author
