"""
    imports
"""
from django.shortcuts import render
from .models import Contact
from . import forms


# Create your views here.
def contactForm(request):
    """
        Contact Form
    """
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()

        form = forms.Contact()
        if request.method == 'POST':
            form = forms.Contact(request.POST)
            html = 'we have recieved this form again'
        else:
            html = 'We will get back to you soon'
    return render(request, 'contact.html', {'html': html, 'form': form})
