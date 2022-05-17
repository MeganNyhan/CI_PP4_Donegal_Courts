# imports
from django.db import models


class Contact(models.Model):
    """
        Contact Model
    """
    first_name = models.CharField(max_length=255, unique=True,
                                  editable=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    subject = models.CharField(max_length=255, null=False, blank=False)
    message = models.TextField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} Subject: {self.subject}"
