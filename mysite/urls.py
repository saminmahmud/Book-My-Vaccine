from django.contrib import admin
from django.urls import path, include, re_path
from mysite import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    
    path('admin/', admin.site.urls),    
    path('', views.index, name='index'),
    path('center/', include('center.urls', namespace='center')),
    path('vaccine/', include('vaccine.urls', namespace='vaccine')),
    path('accounts/', include('user.urls', namespace='user')),
    path('campaign/', include('campaign.urls', namespace='campaign')),
    path('vaccination/', include('vaccination.urls', namespace='vaccination')),
]


admin.site.site_header = "Book My Vaccine"
admin.site.site_title = "Book My Vaccine"
admin.site.index_title = "Admin Panel"