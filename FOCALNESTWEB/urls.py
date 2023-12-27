from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import login_page

urlpatterns = [
    path('', include('FocalNest.urls')),
    path('focalnestadmin/', admin.site.urls),
    path('focalnestadmin/login/', login_page.as_view(), name='admin_login'),
]

admin.site.site_header = ''  # Set your custom site header
admin.site.site_title = ''  # Set your custom site title
admin.site.index_title = ''  # Set your custom index title

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
