from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

admin.site.site_header = 'Content Manager'
admin.site.site_title = 'Content Manager'
admin.site.index_title = 'Atur semua konten web dari sini'

def health_check(request):
    return HttpResponse("OK")

urlpatterns = [
    path('health', health_check),
    path('health/', health_check),
    path('manage-7k2x/', admin.site.urls),
    path('', include('portfolio.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
