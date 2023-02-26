from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('webFrontend.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.index_title = settings.ADMIN_INDEX_TITLE