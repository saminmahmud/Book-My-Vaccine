from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.Signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('change-password/', views.ChangePassword, name='change-password'),
    path('reset-password/', views.ResetPassword, name='reset-password'),
    path('profile-view/', views.Profile_view, name='profile-view'),
    path('profile-update/', views.Profile_update, name='profile-update'),
    path('verify-email/', views.email_verification_request, name='verify-email'),
    path('email/activate/<uid64>/<token>/', views.email_verifier, name='email-activate'),
]