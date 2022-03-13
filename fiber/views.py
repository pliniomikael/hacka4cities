from django.http import JsonResponse
# Create your views here.
from .models import *

def list_bairros(request):
  data = []  

  for bairro in Bairro.objects.all():
    item = {
      "cidade": bairro.cidade.name,
      "nome": bairro.name,
      "perda": float(bairro.loss_sensor)
    }
    data.append(item)

  return JsonResponse(data, content_type="application/json", safe=False)

def list_sensores(request):
  data = []  

  for sensor in Sensor.objects.all():
    item = {
      "id": sensor.id,
      "cidade": sensor.bairro.cidade.name,
      "bairro": sensor.bairro.name,
      "rua": sensor.rua,
      "distancia": float(sensor.distance),
      "perda": float(sensor.splice_loss),
      "geoLocation": {
        "latitude": float(sensor.latitude),
        "longitude": float(sensor.longitude),
      },
      "status": sensor.status
    }
    data.append(item)

  return JsonResponse(data, content_type="application/json", safe=False)
