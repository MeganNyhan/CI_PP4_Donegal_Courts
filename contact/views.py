from django.shortcuts import render
from .models import Contact


# Create your views here.
def contactForm(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        from_email = request.POST.get('from_email')
        message = request.POST.get('message')

        contact.name = name
        contact.from_email = from_email
        contact.message = message
        contact.save()

    return render(request, 'contact.html')
