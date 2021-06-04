from django.db import models

from accounts.models import Profile


# Create your models here.

class Material(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    material_code = models.CharField(max_length=100, blank=True)
    material_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.id)
