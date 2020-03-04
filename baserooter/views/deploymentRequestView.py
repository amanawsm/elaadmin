from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.compat import coreapi, coreschema
from rest_framework.permissions import IsAuthenticated
from baserooter.services import requestsService
from rest_framework.status import *


class createDeploymentRequest(APIView):
    """
    This API is used to create new deployment requests.
    """
    permission_classes = (IsAuthenticated,)
    schema = AutoSchema(manual_fields=[        
        coreapi.Field("program_version",required=True,location="form",schema=coreschema.String()),
        coreapi.Field("version",required=True,location="form",schema=coreschema.String()),
        coreapi.Field("requested_by",required=True,location="form",schema=coreschema.String()),
        coreapi.Field("description",required=True,location="form",schema=coreschema.String()),
        coreapi.Field("technician_id",required=True,location="form",schema=coreschema.String()),
        coreapi.Field("status",required=True,location="form",schema=coreschema.String())
    ])    
    def post(self, request, format=None):
        data = requestsService.createDeploymentRequest(request)
        return Response(data, status=HTTP_200_OK)
        

class getDeploymentRequest(APIView):
    """
    This API is used to retreive all deployment requests.
    """
    permission_classes = (IsAuthenticated,)
    def post(self,request, format=None):
        data = requestsService.getDeploymentRequest(request)
        return Response(data, status=HTTP_200_OK)


class updateDeploymentRequest(APIView):
    """
    This API is used to retreive all deployment requests.
    """
    permission_classes = (IsAuthenticated,)
    schema = AutoSchema(manual_fields=[        
        coreapi.Field("deployment_id",required=True,location="form",schema=coreschema.String()),
        coreapi.Field("status",required=True,location="form",schema=coreschema.String())
    ])
    def put(self, request, format=None):
        data = requestsService.updateDeploymentRequest(request) 
        return Response(data, status=HTTP_200_OK)


        
