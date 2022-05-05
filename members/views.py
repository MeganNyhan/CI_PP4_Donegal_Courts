# Imports
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.view.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
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
    templat_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context
