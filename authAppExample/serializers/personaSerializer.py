from authAppExample.models.persona   import Persona
from rest_framework                  import serializers

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Persona
        fields = ['id','numero_documento','nombre','apellidos','edad','sexo']

        def create(self,validated_data):
            personaInstance = Persona.objects.create(**validated_data)
            return personaInstance

        def to_representation(self,obj):
            persona = Persona.objects.get(id = obj.id)
            return {
                'id'               : persona.id,
                'numero_documento' : persona.numero_documento,
                'nombre'           : persona.nombre,
                'apellidos'        : persona.apellidos,
                'edad'             : persona.edad,
                'sexo'             : persona.sexo
            }
