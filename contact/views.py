"""
    imports
"""
from django.shortcuts import render
from .models import Contact
from django.contrib import messages


# Create your views here.
def contactForm(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()

# If the form is filled out it will save and display the below message

        messages.add_message(request, messages.SUCCESS,
                             'Your message has been sent')

    return render(request, 'contact.html')
