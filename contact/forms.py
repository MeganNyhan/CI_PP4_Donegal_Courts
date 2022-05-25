from django import forms


class Contact(forms.Form):
    """
    contact form
    """
    fields = ('name', 'email', 'message')

    widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.Textarea(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'})
        }
