from django.urls import path
from .views import (
    ClienteListCreate,
    ClienteDetail,
    HabitacionListCreate,
    HabitacionDetail,
    ReservaListCreate,
    ReservaDetail,
    ServicioListCreate,
    ServicioDetail,
    FacturaListCreate,
    FacturaDetail,
)

urlpatterns = [
    path('cliente/', ClienteListCreate.as_view(), name='cliente-list-create'),
    path('cliente/<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),
    
    path('habitacion/', HabitacionListCreate.as_view(), name='habitacion-list-create'),
    path('habitacion/<int:pk>/', HabitacionDetail.as_view(), name='habitacion-detail'),
    
    path('reserva/', ReservaListCreate.as_view(), name='reserva-list-create'),
    path('reserva/<int:pk>/', ReservaDetail.as_view(), name='reserva-detail'),
    
    path('servicio/', ServicioListCreate.as_view(), name='servicio-list-create'),
    path('servicio/<int:pk>/', ServicioDetail.as_view(), name='servicio-detail'),
    
    path('factura/', FacturaListCreate.as_view(), name='factura-list-create'),
    path('factura/<int:pk>/', FacturaDetail.as_view(), name='factura-detail'),
]

