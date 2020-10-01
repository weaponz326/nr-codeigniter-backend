from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Rink(models.Model):
    sender = models.ForeignKey(User, related_name='rink_sender', on_delete=models.DO_NOTHING)
    recipient = models.ForeignKey(User, related_name='rink_recipient', on_delete=models.DO_NOTHING)
    rink_date = models.DateTimeField(auto_now_add=True)
    rink_type = models.CharField(max_length=50, null=True)
    rink_source = models.CharField(max_length=50, null=True)
    comment = models.TextField()

    def __str__(self):
        return str(self.id)
