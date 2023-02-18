import json
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Extra(models.Model):
    address: str = models.CharField(max_length=255)
    altitude: float = models.FloatField(null=True)
    ebikes: int = models.IntegerField(null=True)
    has_ebikes: bool = models.BooleanField(default=True)
    last_updated: int = models.IntegerField(null=True)
    normal_bikes: int = models.IntegerField(null=True)
    payment: list = ArrayField(models.CharField(max_length=255))
    payment_terminal: bool = models.BooleanField(default=True)
    post_code: str = models.CharField(max_length=255)
    renting: int = models.IntegerField(null=True)
    returning: int = models.IntegerField(null=True)
    slots: int = models.IntegerField(null=True)
    uid: str = models.CharField(max_length=255)

    class Meta:
        unique_together = ('uid',)


class Stations(models.Model):
    empty_slots: int = models.IntegerField(null=True)
    extra: Extra = models.ForeignKey('Extra',models.DO_NOTHING, related_name='bike_extra')
    free_bikes: int = models.IntegerField(null=True)
    id_api: str = models.CharField(max_length=255)
    latitude: float = models.FloatField(null=True)
    longitude: float = models.FloatField(null=True)
    name: str = models.CharField(max_length=255)
    timestamp: str = models.CharField(max_length=255)

    class Meta:
        unique_together = ('id_api',)

