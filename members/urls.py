# import views
from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/', PasswordsChangeView.as_view(
         template_name='registration/change-password.html')),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(),
         name='show_profile_page'),
]
