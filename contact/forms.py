# imports
from django import forms
from .models import Contact


class ContactForm(forms.Form):
    """
    This is Contact Form
    This uses a Field level Validation
    """
    model = Contact
    fields = ('first_name', 'last_name', 'contact_email',
              'subject', 'message',)
