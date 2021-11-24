from authAppExample.models.pais      import Pais
from authAppExample.models.prueba    import Prueba
from authAppExample.models.persona   import Persona
from rest_framework                  import serializers

class PruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        fields = ['persona','pais','tipo','resultado','fecha'] 
    
    def to_representation(self,obj):
        prueba   =    Prueba.objects.get(id  = obj.id)
        persona  =    Persona.objects.get(id = obj.persona_id)
        pais     =    Pais.objects.get(id    = obj.pais_id) 
        return {
            'id'     : prueba.id,
            'persona': {
                'id'               : persona.id,
                'numero_documento' : persona.numero_documento,
                'nombre'           : persona.nombre,
                'apellidos'        : persona.apellidos,
                'edad'             : persona.edad,
                'sexo'             : persona.sexo
            },
            'pais'    : {
                'id'     : pais.id,
                'nombre' : pais.nombre
            },
            'tipo'      : prueba.tipo,
            'resultado' : prueba.resultado,
            'fecha'     : prueba.fecha
        } 