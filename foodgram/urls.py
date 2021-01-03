from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler404, handler500, handler400
from django.conf.urls.static import static


handler400 = 'recipes.views.page_bad_request'
handler404 = 'recipes.views.page_not_found'
handler500 = 'recipes.views.server_error'

urlpatterns = [
    path('auth/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('about-author/', lambda x: x, name='about_author'),
    path('tech-stack/', lambda x: x, name='tech_stack'),
    path('api/', include('api.urls')),
    path('', include('recipes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )