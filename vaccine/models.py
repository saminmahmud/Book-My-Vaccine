from django.db import models

class Vaccine(models.Model):
    name = models.CharField("Vaccine Name", max_length=50)
    description = models.TextField()
    number_of_doses = models.IntegerField(default=1)
    interval = models.IntegerField(default=0, help_text="Please provide interval in days")
    storage_temperature = models.IntegerField(null=True, blank=True, help_text="Please provide storage temperature in Celsius")
    minimum_age = models.IntegerField(default=0)

    def __str__(self):
        return self.name
