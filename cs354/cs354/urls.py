from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('comments/', include('django_comments_xtd.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('launch.urls'), name='home'),
    path('lost/', include('lost.urls')),
    path('found/', include('found.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)