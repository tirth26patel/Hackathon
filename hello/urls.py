
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

admin.site.site_header="Subsidi portel Admin portal"
admin.site.site_title="Subsidi portel Admin portal"
# admin.site.index_titler="Subsidi portel Admin portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
