from django.test import TestCase
from django.core import mail

# Create your tests here.


class EmailTest(TestCase):
    def test_send_email(self):
        """
            Send Email
        """
        subject = 'subject'
        message = 'message'
        from_email = 'from_email@test.com'
        recipient_list = ['recipient@test.com']
        mail.send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list
        )
        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)
