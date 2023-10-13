from django.db import models

class Email(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    recipient = models.EmailField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.subject