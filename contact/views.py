from django.shortcuts import render
from .models import Contact


# Create your views here.
def contact(request):
    if request.method == "POST":
        contact = Contact()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        from_email = request.POST.get('from_email')
        message = request.POST.get('message')

        contact.first_name = first_name
        contact.last_name = last_name
        contact.from_email = from_email
        contact.message = message

    return render(request, 'contact.html')
