from django.conf                                      import settings
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from rest_framework.permissions                       import IsAuthenticated
from rest_framework_simplejwt.backends                import TokenBackend

from authAppExample.serializers.paisSerializer        import PaisSerializer
from authAppExample.models.pais                       import Pais

class PaisGetAll(generics.ListAPIView):
    serializer_class = PaisSerializer
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Pais.objects.all()
        return queryset