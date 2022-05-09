# import views
from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCommentView, ContactFormView
from . import views



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'),
    path('contact/', ContactFormView.as_view(), name='contact'),

]
