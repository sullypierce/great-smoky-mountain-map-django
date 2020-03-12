from django.db import models
from marker_type import MarkerType
from marker import Marker
from trip_plan_marker import TripPlanMarker
from django.contrib.auth.models import User


class TripPlan(models.Model):

    created_at = models.DateField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    markers = models.ManyToManyField(Marker, through=TripPlanMarker)


    class Meta:
        ordering = ("created_at",)
        verbose_name = ("order",)
        verbose_name_plural = ("orders",)