from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', include('home.urls',namespace="home")),
    path('', include('splash.urls',namespace="splash")),
    path('accounts/', include('accounts.urls',namespace="accounts")),
    path('about_us/', include('about_us.urls',namespace="about_us")),
    path('doctors/', include('Doctors.urls',namespace="doctors")),
    path('rays/', include('rays.urls',namespace="rays")),
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)