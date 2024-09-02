from django.contrib import admin
from django.urls import path, include

# LLamo a mi archivo settings del core
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('usuarios.urls')),
]


# Esta configuracion es obligatoria cuando yo quiero guardar imagenes en mi sevidor y a su vez quiero que estas 
# imagenes puedan ser consumidas por terceros

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)