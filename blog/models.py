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
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_post")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """
        This orders my blog posts in descending order from the date it was
        created on.
        Oldest to Newest.
        """
        ordering = ['-created_on']

    def str(self):
        """
        Return the post's title string.
        """
        return str(self.title)


class Comment(models.Model):
    """
    This comment model allows the user to leave a comment.
    The information included is name, email, comment and date
    it was created on.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Again this model orders the comments in descending order.
        """
        ordering = ['created_on']

    def __repr__(self):
        """
        Returns an f string of the comments body and name.
        """
        return f'Comment {self.body} by {self.name}'


class Carausel(models.Model):
    """
        This model calls the items for display
    """
    image = models.ImageField(upload_to='pics/%y/%m/%d/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def str(self):
        """
        Return the post's title string.
        """
        return str(self.title)
