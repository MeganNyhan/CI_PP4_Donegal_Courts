"""
    imports
"""
from django.db import models


# Create your models here.
class Contact(models.Model):
    """
        Contact Model for contact section of site
    """
    name = models.CharField(max_length=200)
    from_email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.from_email)
