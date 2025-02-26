from django.contrib.auth import get_user_model
from django.db import models
from campaign.models import Campaign, Slot

User = get_user_model()

class Vaccination(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    is_vaccinated = models.BooleanField(default=False)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.patient.get_full_name()} | {self.campaign.vaccine.name}'
