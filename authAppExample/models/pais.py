from django.db                   import models


class Pais(models.Model):
    id       = models.AutoField(primary_key = True,unique = True)
    nombre   = models.CharField('Username'        ,max_length =20,unique = True)
    