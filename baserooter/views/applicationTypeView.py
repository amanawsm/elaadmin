from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.schemas import AutoSchema
from rest_framework.compat import coreapi, coreschema
from baserooter.services import applicationsViewServices
from rest_framework.status import *

class applicationTypeView(APIView):
    """
    Thsi API is used to obtain all programs/application types based on environment.
    """
    permission_classes = (IsAuthenticated,)
    schema = AutoSchema(manual_fields=[        
        coreapi.Field("environment",required=True,location="form",schema=coreschema.String()),
        
    ])
    
    def post(self, request, format=None):        
        
        data = applicationsViewServices.getApplicationType(request)
        return Response(data, status=HTTP_200_OK)
    