from django.db import models
from .marker_type import MarkerType
from django.contrib.auth.models import User


class Marker(models.Model):

    created_at = models.DateField(auto_now=False, auto_now_add=True)
    lat = models.CharField(max_length=20, null = True)
    long = models.CharField(max_length=20, null = True)
    is_public = models.BooleanField()
    marker_type = models.ForeignKey(MarkerType, on_delete=models.DO_NOTHING, null=True, default=None)
    description = models.CharField(max_length=100, null = True)
    picture_url = models.CharField(max_length=25, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        ordering = ("created_at",)
        verbose_name = ("order",)
        verbose_name_plural = ("orders",)
