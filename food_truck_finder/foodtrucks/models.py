from django.db import models
from django.utils import timezone

class FoodTruck(models.Model):
    locationid = models.PositiveIntegerField(default=0, null=True)
    Applicant = models.CharField(max_length=255, default='', null=True)
    FacilityType = models.CharField(max_length=100, default='', null=True)
    cnn = models.PositiveIntegerField(default=0, null=True)
    LocationDescription = models.CharField(max_length=255, default='', null=True)
    Address = models.CharField(max_length=255, default='', null=True)
    blocklot = models.CharField(max_length=255, default='', null=True)
    block = models.CharField(max_length=255, default='', null=True)
    lot = models.CharField(max_length=255, default='', null=True)
    permit = models.CharField(max_length=255, default='', null=True)
    Status = models.CharField(max_length=100, default='', null=True)
    FoodItems = models.TextField(default='', null=True)
    X = models.FloatField(default=0.0, null=True)
    Y = models.FloatField(default=0.0, null=True)
    latitude = models.FloatField(default=0.0, null=True)
    longitude = models.FloatField(default=0.0, null=True)
    Schedule = models.CharField(max_length=255, default='', null=True)
    dayshours = models.CharField(max_length=255, default='', null=True)
    NOISent = models.CharField(max_length=255, default='', blank=True, null=True)
    Approved = models.CharField(max_length=255, default='', null=True)
    Received = models.CharField(max_length=255, default='', null=True)
    PriorPermit = models.IntegerField(default=0, null=True)
    ExpirationDate = models.CharField(max_length=255, default='', null=True)
    Location = models.CharField(max_length=255, default='', null=True)
    FirePreventionDistricts = models.IntegerField(default=0, null=True)
    PoliceDistricts = models.IntegerField(default=0, null=True)
    SupervisorDistricts = models.IntegerField(default=0, null=True)
    ZipCodes = models.IntegerField(default=0, null=True)
    Neighborhoods_old = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.Applicant
