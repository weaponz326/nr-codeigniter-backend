from django.db import models

from accounts.models import Profile


# Create your models here.

class Rink(models.Model):
    sender = models.ForeignKey(Profile, related_name='rink_sender', on_delete=models.DO_NOTHING)
    recipient = models.ForeignKey(Profile, related_name='rink_recipient', on_delete=models.DO_NOTHING)
    rink_date = models.DateTimeField(auto_now_add=True)
    rink_type = models.CharField(max_length=50, null=True)
    rink_source = models.IntegerField(null=True)
    comment = models.TextField()

    def __str__(self):
        return str(self.id)
