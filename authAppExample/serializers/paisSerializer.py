from authAppExample.models.pais    import Pais
from rest_framework                import serializers

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Pais
        fields = ['nombre']

    def create(self,validated_data):
        paisInstance = Pais.objects.create(**validated_data)
        return paisInstance

    def to_representation(self,obj):
        pais = Pais.objects.get(id = obj.id)
        return {
            'id'     : pais.id,
            'nombre' : pais.nombre
        }    
