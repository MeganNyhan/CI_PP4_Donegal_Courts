"""
    imports
"""
from django.db import models
from django import forms


# Create your models here.
class Contact(models.Model):
    """
        Contact Model for contact section of site
    """
    name = models.CharField(max_length=150, blank=False, null=True)
    email = models.EmailField(default='DEFAULT VALUE', blank=True, null=True)
    message = models.CharField(max_length=1500, blank=False, null=True,
                               widget=forms.TextInput(attrs={'size': '80'}))

    def __str__(self):
        return str(self.email)
