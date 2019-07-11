from django.urls import path
from agrishop import views as core_views
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login', views.login, name='login'),
    path('registro/', core_views.signup, name='signup'),
    path('agregarProducto', views.cargarFormularioProducto, name='cargarFormularioProducto'),
    path('guardarProducto', views.guardarProducto, name='guardarProducto'),
    path('listadoProductos', views.listadoProductos, name='listadoProductos'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)