from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.compat import coreapi, coreschema
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import *
from baserooter.services import requestsService

class createNormalRequest(APIView):
    """
    This API is used to create normal requests.
    """
    permission_classes = [IsAuthenticated]
    schema = AutoSchema(manual_fields=[        
        coreapi.Field("title",required=True,location="form",schema=coreschema.String()),
        coreapi.Field("description",required=True,location="form",schema=coreschema.String()),
        coreapi.Field("attachment",required=False,location="form",schema=coreschema.String()),
        coreapi.Field("status",required=True,location="form",schema=coreschema.String()),
        coreapi.Field("requested_by",required=True,location="form",schema=coreschema.String())
    ]) 
       
    def post(self, request, format=None):        
        data = requestsService.createNormalRequest(request) 
        return Response(data, status=HTTP_200_OK)      
        

class retrieveNormalRequest(APIView):
    """
    This API is used to fetched the records
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        data = requestsService.getNormalRequest(request)        
        return Response(data, status=HTTP_200_OK)

class updateNormalRequest(APIView):
    """
    This API is used to fetched the records
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        data = requestsService.updateNormalRequest(request)        
        return Response(data, status=HTTP_200_OK)
        
