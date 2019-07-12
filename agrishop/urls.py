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
    path('mapa',views.mapa,name='mapa'),
    path('administrarProductos/<int:usuario_id>', views.administrarProductos, name='administrarProductos'),
    path('borrarProducto/<int:producto_id>', views.borrarProducto, name='borrarProducto'),
    path('detalleProducto/<int:producto_id>', views.detalleProducto, name='detalleProducto'),
    path('modificarProducto/<int:producto_id>', views.modificarProducto, name='modificarProducto'),
    path('confirmarModificacion/<int:producto_id>', views.confirmarModificacion, name='confirmarModificacion'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)