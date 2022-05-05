# Imports
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from blog.models import Carousel
from blog.models import Profile


class PasswordsChangeView(PasswordChangeView):
    """
        Chnage Password function
    """
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class UserRegisterView(generic.CreateView):
    """
        Login function
    """
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    """
        Edit User Function
    """
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordChangedForm(PasswordChangeForm):
    """
    Change Password VForm Views
    """
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


class ShowProfilePageView(DetailView):
    """
    Show Profile View
    """
    model = Profile
    template_name = 'registration/user_profile.html'
