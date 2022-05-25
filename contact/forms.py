from django import forms


class Contact(forms.Form):
    """
    contact form
    """
    name: forms.CharField(max_length=50)
    email: forms.CharField(max_length=50)
    message: forms.CharField(max_length=2000)
       
