# import views
from django.urls import path
from .views import HomeView, PostDetailView, UpdatePostView, DeletePostView, AddCommentView, LikeView, contactView, successView
from . import views



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('contact/', contactView, name='contact'),
    path('success', successView, name='success'),


]
