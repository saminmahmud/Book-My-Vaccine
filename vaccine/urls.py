from django.urls import path
from vaccine import views

app_name = 'vaccine'

urlpatterns = [
    path('', views.VaccineList.as_view(), name='list'),
    path('<int:id>/', views.VaccineDetail.as_view(), name='detail'),
    path('create/', views.VaccineCreate.as_view(), name='create'),
    path('update/<int:id>/', views.VaccineUpdate.as_view(), name='update'),
    path('delete/<int:id>/', views.VaccineDelete.as_view(), name='delete'),
]