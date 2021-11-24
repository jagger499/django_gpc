from rest_framework                                import status, views
from rest_framework.response                       import Response
from rest_framework_simplejwt.serializers          import TokenObtainPairSerializer

from authAppExample.serializers.paisSerializer     import PaisSerializer

class PaisCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = PaisSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status = status.HTTP_201_CREATED)