from django.db import models

from accounts.models import Profile
from module_workers.models import Worker


# Create your models here.

class Roster(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    roster_code = models.CharField(max_length=20, blank=True)
    roster_name = models.CharField(max_length=100, blank=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)

    def __str__(self):
        return str(self.id)

class Shift(models.Model):
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
    shift_name = models.CharField(max_length=100, blank=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    def __str__(self):
        return str(self.id)

class Batch(models.Model):
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
    batch_name = models.CharField(max_length=100, blank=True)
    batch_symbol = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.id)

class WorkerPersonnel(models.Model):
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, null=True, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class RosterDay(models.Model):
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
    day = models.DateField(null=True, blank=True)

class RosterSheet(models.Model):
    roster_day = models.ForeignKey(RosterDay, null=True, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, null=True, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, null=True, on_delete=models.CASCADE)
