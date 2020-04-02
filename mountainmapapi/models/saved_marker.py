from django.db import models
from .marker_type import MarkerType
from .marker import Marker
from django.contrib.auth.models import User


class SavedMarker(models.Model):

    created_at = models.DateField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    marker = models.ForeignKey(Marker, on_delete=models.CASCADE)


    class Meta:
        ordering = ("created_at",)
        verbose_name = ("saved_marker",)
        verbose_name_plural = ("saved_markers",)