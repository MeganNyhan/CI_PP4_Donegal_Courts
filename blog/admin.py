# imports from models.py
from django.contrib import admin
from .models import Post, Comment, Profile, Carousel


admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Carousel)
