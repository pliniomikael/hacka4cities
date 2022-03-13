from django.db import models
from django.utils.translation import gettext_lazy as _


SENSOR_STATUS = [
    ('Normal', 'NORMAL'),
    ('Vazamento', 'VAZAMENTO'),
    ('Em Manutenção', 'EM MANUTENCAO'),
    ('Reparo concluído', 'REPARO CONCLUIDO'),
]


class Cidade(models.Model):

    name = models.CharField(_("Cidade"), max_length=50)

    class Meta:
        verbose_name = _("Cidade")
        verbose_name_plural = _("Cidades")

    def __str__(self):
        return self.name

class Bairro(models.Model):
    cidade = models.ForeignKey("fiber.Cidade", verbose_name=_("Cidade"), related_name="bairros", on_delete=models.CASCADE)
    name = models.CharField(_("Bairro"), max_length=50)


    @property
    def loss_sensor(self):
        value = 0
        for sensor in self.sensores.all():
            value += sensor.splice_loss
        return value

    class Meta:
        verbose_name = _("Bairro")
        verbose_name_plural = _("Bairros")

    def __str__(self):
        return self.name


# Create your models here.
class Sensor(models.Model):

    bairro = models.ForeignKey("fiber.Bairro", verbose_name=_("Bairro"), related_name='sensores', on_delete=models.CASCADE)
    rua = models.CharField(_("Rua"), max_length=50, null=True, blank=True)
    distance = models.DecimalField(_("Distancia"), max_digits=10, decimal_places=3 )
    splice_loss = models.DecimalField(_("Perda"), max_digits=10, decimal_places=3)
    status = models.CharField(_("Status"), choices=SENSOR_STATUS, max_length=50,  null=True, blank=True)
    latitude = models.DecimalField(_("Latitude"), max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(_("logitude"), max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name = _("sensor")
        verbose_name_plural = _("sensors")

    def __str__(self):
        return self.bairro.name


