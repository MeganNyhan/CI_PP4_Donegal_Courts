"""
    imports
"""
from .models import Contact
from django.contrib import messages


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
        messages.success(request, 'Your message has been sent')
