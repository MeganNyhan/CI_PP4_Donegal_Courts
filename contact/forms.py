from django import forms


class ContactForm(forms.Form):
    """
    This is Contact Form
    This uses a Field level Validation
    """
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
