from django.urls import path
from measurement.views import SensorViews, SensorsViews, MeasurementViews


urlpatterns = [
                path('sensors/', SensorViews.as_view()),
                path('sensors/<pk>/', SensorsViews.as_view()),
                path('measurements/', MeasurementViews.as_view()),
              ]