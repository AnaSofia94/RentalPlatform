from django.db import models
from django.contrib.auth.models import User

class HomeListing(models.Model):
    title = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_wheelchair_friendly = models.BooleanField(default=False)
    # other fields

    def __str__(self):
        return self.title


class TenantListing(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SavedSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255, null=True, blank=True)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_wheelchair_friendly = models.BooleanField(default=False)
    # other criteria

    def __str__(self):
        return self.name