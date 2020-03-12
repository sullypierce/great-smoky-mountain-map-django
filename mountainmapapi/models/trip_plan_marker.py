from django.db import models


class TripPlanMarker(models.Model):

    trip_plan = models.ForeignKey("TripPlan", on_delete=models.CASCADE)
    marker = models.ForeignKey("Marker", on_delete=models.CASCADE)

    class Meta:
        ordering = ("marker",)