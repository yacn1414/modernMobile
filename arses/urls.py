
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path,include
admin.site.site_header = "admin panel"
admin.site.site_title="yacn"
admin.site.index_title="اینا امکانات استفاده کن (در ضمن این سایت شدیدا در حال توسعه میباشد)"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('',include('details.urls')),
    path('',include('Users.urls')),
    path('',include('django.contrib.auth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()