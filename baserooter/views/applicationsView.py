from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.schemas import AutoSchema
from rest_framework.compat import coreapi, coreschema
from rest_framework.status import *
from baserooter.services import applicationsViewServices


class getApplications(APIView):
    """
    This API is used to retrieve all applications using environment and application_type parameters.
    """
    permission_classes = [IsAuthenticated]
    schema = AutoSchema(manual_fields=[        
        coreapi.Field("environment",required=True,location="form",schema=coreschema.String()),
        coreapi.Field("app_type_id",required=True,location="form",schema=coreschema.String()),
    ])

    def post(self, request, format=None):            
        data = applicationsViewServices.getApplications(request)
        return Response(data, status=HTTP_200_OK)


class getAppdataView(APIView):
    """
    This API is used to retrieve all applications using environment and application_type parameters.
    """
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = applicationsViewServices.getAppdataService(request)
        return Response(data, status=HTTP_200_OK)
class getProgramDataView(APIView):
    """
    This API is used to retrieve all applications using environment and application_type parameters.
    """
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = applicationsViewServices.getProgramData(request)
        return Response(data, status=HTTP_200_OK)

class updateProgramVersion(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = applicationsViewServices.updateProgramVersion(request)
        return Response(data, status=HTTP_200_OK)


