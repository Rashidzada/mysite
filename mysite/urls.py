
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static,settings

admin.site.site_title = "My Profile"
admin.site.site_header = "My Profile"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
