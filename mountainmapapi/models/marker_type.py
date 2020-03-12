from django.db import models
from django.db.models import F


class MarkerType(models.Model):

    type_name = models.CharField(max_length=25)


    def __str__(self):
        return f'{self.type_name}'