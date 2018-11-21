from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [

	# admin/
    url(r'^admin/', admin.site.urls),

    # dashboard/
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),

    # forum/
    url(r'^forum/', include('forum.urls', namespace='forum')),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)