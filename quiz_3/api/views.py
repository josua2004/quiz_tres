from rest_framework import generics, status
from .models import Cliente, Habitacion, Reserva, Servicio, Factura
from .serializers import ClienteSerializer, HabitacionSerializer, ReservaSerializer, ServicioSerializer, FacturaSerializer
from .mixins import CustomResponseMixin


class ClienteListCreate(CustomResponseMixin, generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    success_message = "Cliente creado exitosamente."

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return self.custom_response(serializer.data, status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        self.success_message = "Lista de clientes obtenida exitosamente."
        return self.custom_response(serializer.data, status.HTTP_200_OK)

class ClienteDetail(CustomResponseMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        self.success_message = "Cliente actualizado exitosamente."
        return self.custom_response(serializer.data, status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.success_message = "Cliente eliminado exitosamente."
        self.perform_destroy(instance)
        return self.custom_response({}, status.HTTP_204_NO_CONTENT)


class HabitacionListCreate(CustomResponseMixin, generics.ListCreateAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer
    success_message = "Habitación creada exitosamente."

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return self.custom_response(serializer.data, status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        self.success_message = "Lista de habitaciones obtenida exitosamente."
        return self.custom_response(serializer.data, status.HTTP_200_OK)

class HabitacionDetail(CustomResponseMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        self.success_message = "Habitación actualizada exitosamente."
        return self.custom_response(serializer.data, status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.success_message = "Habitación eliminada exitosamente."
        self.perform_destroy(instance)
        return self.custom_response({}, status.HTTP_204_NO_CONTENT)



class ReservaListCreate(CustomResponseMixin, generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    success_message = "Reserva creada exitosamente."

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return self.custom_response(serializer.data, status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        self.success_message = "Lista de reservas obtenida exitosamente."
        return self.custom_response(serializer.data, status.HTTP_200_OK)

class ReservaDetail(CustomResponseMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        self.success_message = "Reserva actualizada exitosamente."
        return self.custom_response(serializer.data, status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.success_message = "Reserva eliminada exitosamente."
        self.perform_destroy(instance)
        return self.custom_response({}, status.HTTP_204_NO_CONTENT)


class ServicioListCreate(CustomResponseMixin, generics.ListCreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    success_message = "Servicio creado exitosamente."

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return self.custom_response(serializer.data, status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        self.success_message = "Lista de servicios obtenida exitosamente."
        return self.custom_response(serializer.data, status.HTTP_200_OK)

class ServicioDetail(CustomResponseMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        self.success_message = "Servicio actualizado exitosamente."
        return self.custom_response(serializer.data, status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.success_message = "Servicio eliminado exitosamente."
        self.perform_destroy(instance)
        return self.custom_response({}, status.HTTP_204_NO_CONTENT)


class FacturaListCreate(CustomResponseMixin, generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    success_message = "Factura creada exitosamente."

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return self.custom_response(serializer.data, status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        self.success_message = "Lista de facturas obtenida exitosamente."
        return self.custom_response(serializer.data, status.HTTP_200_OK)

class FacturaDetail(CustomResponseMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        self.success_message = "Factura actualizada exitosamente."
        return self.custom_response(serializer.data, status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.success_message = "Factura eliminada exitosamente."
        self.perform_destroy(instance)
        return self.custom_response({}, status.HTTP_204_NO_CONTENT)
