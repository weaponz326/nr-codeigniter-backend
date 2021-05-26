from django.db import models

from accounts.models import Profile


# Create your models here.

class Meeting(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    main_activity = models.CharField(max_length=100, blank=True)
    meeting_date = models.DateField(null=True)
    meeting_time = models.TimeField(null=True)
    location = models.CharField(max_length=100, blank=True)
    all_activities = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)
