from django.db import models

class ServicesOffered(models.Model):
    serviceName = models.CharField(max_length=255, null=False, blank=False)
    priceRange = models.CharField(max_length=255, null=False, blank=False)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.serviceName}"

class ServiceLocation(models.Model): #home service / store
    location = models.CharField(max_length=255, null=False, blank=False)
    additionalFee = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.location}"
