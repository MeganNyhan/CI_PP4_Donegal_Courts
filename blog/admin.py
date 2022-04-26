# imports from models.py
from django.contrib import admin
from .models import Post, Comment
# from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Post)
admin.site.register(Comment)
