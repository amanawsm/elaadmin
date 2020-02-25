from rest_framework.permissions import IsAuthenticated, AllowAny
from baserooter.services.users import userViewServices
from rest_framework.schemas import AutoSchema
from rest_framework.compat import coreapi, coreschema
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.status import *



class createUserView(APIView):
    """
    Thsi API is used to register new users into our databases
    """
    permission_classes = [AllowAny]
    schema = AutoSchema(manual_fields=[        
            coreapi.Field("email",required=True,location="form",schema=coreschema.String()),
            coreapi.Field("password",required=True,location="form",schema=coreschema.String()),
            coreapi.Field("first_name",required=True,location="form",schema=coreschema.String()),
            coreapi.Field("last_name",required=True,location="form",schema=coreschema.String())
        ])    
    
    def post(self,request,format=None):
        data = userViewServices.createUsers(request)
        return Response(data, status=HTTP_200_OK)


class loginUserView(APIView):
    """
    Thsi API is used to authenticate users with username and password. 
    """ 
    permission_classes = [AllowAny]
    schema = AutoSchema(manual_fields=[        
            coreapi.Field("username",required=True,location="form",schema=coreschema.String()),
            coreapi.Field("password",required=True,location="form",schema=coreschema.String()),
        ])    

    def post(self,request,format=None):
        result = userViewServices.userLogin(request)
        return Response(result, status=HTTP_200_OK)



class updatePasswordView(APIView):
    """
    Thsi API is used to change password for authenticated user
    """
    permission_classes = [IsAuthenticated]

    schema = AutoSchema(manual_fields=[ 
            coreapi.Field("password",required=True,location="form",schema=coreschema.String())
        ])

    def put(self, request, format=None): 
        data = userViewServices.updateUser(request) 
        return Response(data, status=HTTP_200_OK)

class logoutView(APIView):
    """
    This method is used to logout active user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data = userViewServices.logoutUser(request)
        return Response(data, status=HTTP_200_OK)

