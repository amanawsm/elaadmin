from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from baserooter.services import environmentService
from rest_framework.schemas import AutoSchema
from rest_framework.compat import coreapi, coreschema
from rest_framework.status import *


class environmentView(APIView):
    """
    Thsi API is used to obtain all environments.
    """
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):        
        data = environmentService.getEnvironments(request)
        return Response(data, status= HTTP_200_OK)
        