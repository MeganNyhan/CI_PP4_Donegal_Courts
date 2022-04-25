"""
imports from Django.
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

# This tuple will keep track of drafted posts and published posts
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    This post model will allow me to post onto the
    site, and create the required variables fields.
    """
    title = models.CharField(max_length=255, unique=True)
    title_tag = models.CharField(max_length=200)
    featured_image = CloudinaryField('image', default='placeholder')
    snippet = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

