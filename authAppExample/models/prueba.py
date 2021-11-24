from django.db      import models
from .persona       import Persona
from .pais          import Pais

class Prueba(models.Model):
    id         = models.AutoField(primary_key=True)
    persona    = models.ForeignKey(Persona , related_name='prueba_persona', on_delete=models.CASCADE)
    pais       = models.ForeignKey(Pais       , related_name='prueba_pais'   , on_delete=models.CASCADE)
    tipo       = models.CharField('tipo'        , max_length  = 20)
    resultado  = models.BooleanField('resultado',default = True)
    fecha      = models.DateTimeField('fecha')