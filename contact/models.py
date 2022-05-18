from django.db import models

# Create your models here.


class Contact(models.Model):
    """
        Contact Model
    """
    first_name = models.CharField(max_length=200, null=False, editable=False)
    last_name = models.CharField(max_length=200, null=False, editable=False)
    from_email = models.EmailField(max_length=200, null=False, editable=False)
    subject = models.CharField(max_length=200, null=False, editable=False)
    message = models.TextField(max_length=2000, null=False, editable=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} Subject: {self.subject}"
