"""
imports from Django.
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.core.validators import validate_slug, validate_email

# This tuple will keep track of drafted posts and published posts
STATUS = ((0, "Draft"), (1, "Published"))


class Profile(models.Model):
    """ 
    Creates User Profile Model
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = CloudinaryField('image', default='placeholder')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)


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


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


class Carousel(models.Model):
    """
        Carousel Model for profile page
    """
    image = CloudinaryField('image', default='placeholder', blank=False)
    title = models.CharField(max_length=150, unique=True, blank=False)
    sub_title = models.CharField(max_length=150, unique=True, blank=False)

    def __str__(self):
        return str(self.title)

