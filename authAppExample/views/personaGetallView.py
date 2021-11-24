from django.conf                                      import settings
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from rest_framework.permissions                       import IsAuthenticated
from rest_framework_simplejwt.backends                import TokenBackend

from authAppExample.serializers.personaSerializer     import PersonaSerializer
from authAppExample.models.persona                    import Persona

class PersonaGetAllView(generics.ListAPIView):
    serializer_class = PersonaSerializer
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Persona.objects.all()
        return queryset