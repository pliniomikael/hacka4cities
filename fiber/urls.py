from django.urls import path
from .views import list_bairros, list_sensores
urlpatterns = [
  path('bairros/', list_bairros, name='list_bairros'),
  path('sensores/', list_sensores, name='list_sensores')
]

