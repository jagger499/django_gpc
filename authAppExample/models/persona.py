from django.db                   import models


class Persona(models.Model):
    id                =  models.AutoField(primary_key=True     ,unique = True)
    numero_documento  =  models.IntegerField('numero_documento',unique = True)
    nombre            =  models.CharField('nombre'          ,max_length = 20)
    apellidos         =  models.CharField('apellidos'       ,max_length = 20)
    edad              =  models.IntegerField('edad')  
    sexo              =  models.CharField('sexo'            ,max_length = 10)

