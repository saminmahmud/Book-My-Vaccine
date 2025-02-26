from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from campaign.forms import CampaignForm, SlotForm
from campaign.models import Campaign, Slot
from vaccination.models import Vaccination


class CampaignListView(LoginRequiredMixin, generic.ListView):
    model = Campaign
    template_name = 'campaign/campaign-list.html'
    paginate_by = 10
    ordering = ['-id']


class CampaignDetailView(LoginRequiredMixin, generic.DetailView):
    model = Campaign
    template_name = 'campaign/campaign-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["registration"] = Vaccination.objects.filter(campaign = self.kwargs['pk']).count()
        return context


class CreateCampaignView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Campaign
    form_class = CampaignForm
    permission_required = ("campaign.add_campaign",)
    template_name = 'campaign/campaign-create.html'
    success_message = "Campaign created successfully"
    success_url = reverse_lazy("campaign:campaign-list")


class UpdateCampaignView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Campaign
    form_class = CampaignForm
    template_name = 'campaign/campaign-update.html'
    permission_required = ("campaign.change_campaign",)
    success_message = "Campaign updated successfully"
    success_url = reverse_lazy("campaign:campaign-list")


class DeleteCampaignView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Campaign
    template_name = 'campaign/campaign-delete.html'
    permission_required = ("campaign.delete_campaign",)
    success_message = "Campaign deleted successfully"
    success_url = reverse_lazy("campaign:campaign-list")


class SlotListView(LoginRequiredMixin, generic.ListView):
    model = Slot
    template_name = 'campaign/slot-list.html'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Slot.objects.filter(campaign=self.kwargs['campaign_id']).order_by('id')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["campaign_id"] = self.kwargs['campaign_id']
        return context



class SlotDetailView(LoginRequiredMixin, generic.DetailView):
    model = Slot
    template_name = 'campaign/slot-detail.html'


class CreateSlotView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Slot
    form_class = SlotForm
    permission_required = ("campaign.add_slot",)
    template_name = 'campaign/slot-create.html'
    success_message = "Slot created successfully"
    
    def get_success_url(self):
        return reverse_lazy('campaign:slot-list', kwargs={'campaign_id': self.kwargs['campaign_id']})
    
    def get_initial(self):
        initial = super().get_initial()
        initial['campaign'] = Campaign.objects.get(id=self.kwargs['campaign_id'])
        return initial
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['campaign_id'] = self.kwargs['campaign_id']
        return kwargs
    

class UpdateSlotView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Slot
    form_class = SlotForm
    template_name = 'campaign/slot-update.html'
    permission_required = ("campaign.change_slot",)
    success_message = "Slot updated successfully"
    
    def get_success_url(self):
        return reverse_lazy('campaign:slot-list', kwargs={'campaign_id': self.kwargs['campaign_id']})
    
    def get_initial(self):
        initial = super().get_initial()
        initial['campaign'] = Campaign.objects.get(id=self.kwargs['campaign_id'])
        return initial
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['campaign_id'] = self.kwargs['campaign_id']
        return kwargs
    

class DeleteSlotView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Slot
    template_name = 'campaign/slot-delete.html'
    permission_required = ("campaign.delete_slot",)
    success_message = "Slot deleted successfully"
    
    def get_success_url(self):
        return reverse_lazy('campaign:slot-list', kwargs={'campaign_id': self.get_object().campaign.id})