from django.conf                                      import settings
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from rest_framework.permissions                       import IsAuthenticated
from rest_framework_simplejwt.backends                import TokenBackend

from authAppExample.serializers.pruebaSerializer      import PruebaSerializer
from authAppExample.models.pais                       import Pais
from authAppExample.models.prueba                     import Prueba
from authAppExample.models.persona                    import Persona

class PruebaGetAllView(generics.ListAPIView):
    serializer_class = PruebaSerializer
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Prueba.objects.all()
        return queryset


class PruebaDetailView(generics.RetrieveAPIView):
    serializer_class   =        PruebaSerializer
    permission_classes =      (IsAuthenticated,)
    queryset           =    Prueba.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PruebaCreateView(generics.CreateAPIView):
    serializers_class  = PruebaSerializer
    permission_classes = (IsAuthenticated, )
    
    def post(self, request, *args, **kwargs):                                                      
        serializer = PruebaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data , status=status.HTTP_201_CREATED)

class PruebaUpdateView(generics.UpdateAPIView):
    serializer_class  = PruebaSerializer
    permission_classes = (IsAuthenticated, )
    queryset           = Prueba.objects.all()

    def update(self, request, *args, **kwargs):
        serializer = PruebaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super().update(request, *args, **kwargs)

class PruebaDeleteView(generics.DestroyAPIView):
    serializer_class  = PruebaSerializer
    permission_classes = (IsAuthenticated, )
    queryset           = Prueba.objects.all()
    
    def deliete(self, request, *args, **kwargs):
        serializer = PruebaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super().destroy(request, *args, **kwargs)            