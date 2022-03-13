from django.contrib import admin
from .models import Cidade, Bairro, Sensor
# Register your models here.
admin.site.site_header = 'Painel Administrativo Fiber Sensor'

class SensorAdmin(admin.ModelAdmin):
  search_fields = ['bairro__name']
  list_display = (
    'cidade_name',
    'bairro_name', 
    'rua', 
    'distance', 
    'splice_loss', 
    'status', 
    'latitude',  
    'longitude')
  
  @admin.display(description='Bairro')
  def bairro_name(self, obj):
    return obj.bairro.name
  
  @admin.display(description='Cidade')
  def cidade_name(self, obj):
    return obj.bairro.cidade.name

admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(Sensor, SensorAdmin)