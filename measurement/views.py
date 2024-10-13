from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorViews(ListAPIView):
    """Отображение списка всех датчиков и создание новых датчиков.
       Метод post создает новый датчик и возвращает его данные с кодом состояния.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SensorsViews(RetrieveUpdateAPIView):
    """Чтение, обновление и удаление существующих датчиков.
       Метод get возвращает данные датчика по Номеру датчика
       Методы put и patch обновляют данные датчика.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    lookup_field = 'pk'

    def get(self, request, pk):
        sensor = self.get_queryset().get(id=pk)
        serializer = SensorDetailSerializer(sensor)
        return Response(serializer.data)

    def get_object(self):
        return self.get_queryset().get(id=self.kwargs['pk'])

    def put(self, request, *args, **kwargs):
        sensor = self.get_object()
        serializer = self.serializer_class(sensor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        sensor = self.get_object()
        serializer = self.serializer_class(sensor, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Изменено успешно."})


class MeasurementViews(ListAPIView):
    """Для добавления температуры.
       Метод post создает новое измерение с указанием даты, вермени и возвращает его данные с кодом состояния
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)