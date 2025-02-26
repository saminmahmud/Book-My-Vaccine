from django.urls import path
from campaign import views

app_name = "campaign"

urlpatterns = [
    path("", views.CampaignListView.as_view(), name="campaign-list"),
    path("<int:pk>/", views.CampaignDetailView.as_view(), name="campaign-detail"),
    path("create/", views.CreateCampaignView.as_view(), name="campaign-create"),
    path("update/<int:pk>/", views.UpdateCampaignView.as_view(), name="campaign-update"),
    path("delete/<int:pk>/", views.DeleteCampaignView.as_view(), name="campaign-delete"),
    path("<int:campaign_id>/slot/", views.SlotListView.as_view(), name="slot-list"),
    path("slot/<int:pk>/", views.SlotDetailView.as_view(), name="slot-detail"),
    path("<int:campaign_id>/slot/create", views.CreateSlotView.as_view(), name="slot-create"),
    path("<int:campaign_id>/slot/update/<int:pk>/", views.UpdateSlotView.as_view(), name="slot-update"),
    path("slot/delete/<int:pk>/", views.DeleteSlotView.as_view(), name="slot-delete")
]