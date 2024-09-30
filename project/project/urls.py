from django.contrib import admin
from django.urls import path
from apps.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('index/', index, name='index'),
    path('1/<int:id>/', nmadur),
    path('a/<int:id>/', detail, name='detail'),
    path('form/', Form, name='form'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)