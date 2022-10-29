from django.db import models


class Requester(models.Model):
    from_location = models.CharField(max_length=255, null=False)
    to_location = models.CharField(max_length=255, null=False)
    date_time = models.DateTimeField()
    is_flexible = models.BooleanField(default=False)
    no_of_assets = models.IntegerField()
    asset_type = models.CharField(max_length=255, null=False)
    asset_sensitivity = models.CharField(max_length=255, null=False)
    whom_to_deliver = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=255, null=False)


class Rider(models.Model):
    from_location = models.CharField(max_length=255, null=False)
    to_location = models.CharField(max_length=255, null=False)
    date_time = models.DateTimeField()
    is_flexible = models.BooleanField(default=False)
    no_of_assets = models.IntegerField()
    travel_medium = models.CharField(max_length=255, null=False)
    is_applied = models.BooleanField(default=False)
    status = models.CharField(max_length=255, null=False, default='NOT_APPLIED')

class RequesterRiderMapper(models.Model):
    requester_id =  models.IntegerField()
    rider_id =  models.IntegerField()
    is_invalid = models.BooleanField(default=False)

