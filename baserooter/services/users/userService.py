import requests
from baserooter.utils import *
from django.contrib.auth import login, logout,authenticate
from baserooter.serializers.users import userSerializer
from rest_framework.status import HTTP_201_CREATED,HTTP_200_OK,HTTP_204_NO_CONTENT,HTTP_400_BAD_REQUEST
from rest_framework_jwt.settings import api_settings
import jwt
from rooter import settings
from django.contrib.auth import get_user_model

User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class userViewServices():

    def user_login_validation(request):
        username = request.data.get('username',None)
        password = request.data.get('password',None)
        result ={}
        if username and password:
            user_instance = User.objects.filter(email=username)
            if len(user_instance)==0:
                result['error'] = RECORD_NOT_FOUND
            else:
                if user_instance[0].check_password(password):                    
                    result['password'] = password
                    result['id'] = user_instance[0].id
                    result['email'] = user_instance[0].email
                    result['first_name'] = user_instance[0].first_name
                    result['last_name'] = user_instance[0].last_name  
                else:
                    result['error'] = DETAILS_INCORRECT                
        else:
            result['error'] = DETAILS_INCORRECT
        return result


    
    def userLogin(request):
        """
        This method is used for user login.
        """
        
        data = userViewServices.user_login_validation(request)
        if len(data) == 1:
            result = {'code':HTTP_400_BAD_REQUEST,'message':DETAILS_INCORRECT}            
        else:
            data1 = {
                    'username':data['email'],'password':data['password'],
                }
            user = authenticate(username=data['email'], password=data['password'])
            login(request,user)
            payload = jwt_payload_handler(user)
            token = jwt.encode(payload, settings.SECRET_KEY)
            domain = request.get_host()
            del data["password"]
            details = {
                            'token':token,'details': data
                        }
            result = {'data':details,'code':HTTP_200_OK,'message':OK}
        return result

    def validate_user_creation(request):
        data ={}        
        email = request.data.get('email',None)
        password = request.data.get('password',None)
        first_name = request.data.get('first_name',None)
        last_name = request.data.get('last_name',None)
        if email and password and first_name:
            if '@' not in str(email) and '.' not in str(email):
                data['error'] = 'please provide valid email address'                            
            else:
                user_data = User.objects.filter(email=email)
                if len(user_data)>0:
                    data['error'] = 'eamil already exists'                                       
                else:
                    data['email']=email
                    data['password']=password
                    data['first_name']=first_name
                    data['last_name']=last_name
        else:
            data['error'] = DETAILS_INCORRECT
        return data     
                    

    def createUsers(request):
        """
        This method is used to validate userdata and create new users
        """
        data = userViewServices.validate_user_creation(request)
        if len(data)==1:
            result = {'data':data, 'code':HTTP_400_BAD_REQUEST,'message':FAIL}
        else:
            serializer = userSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                result = {'data':serializer.data, 'code':HTTP_201_CREATED,'message':OK}        
            else:
                result = {'data':serializer.errors, 'code':HTTP_400_BAD_REQUEST,'message':FAIL}       
        return result

    def updateUser(request):
        """
        This method is used to update users password.
        """
        serializer = userSerializer(
                    request.user, data=request.data, partial=True
                )
        if serializer.is_valid():        
            serializer.save()
            result = {'data':serializer.data,'code':HTTP_200_OK, 'message':OK}
            return result
        else:
            result = {'data':serializer.errors,'code':HTTP_400_BAD_REQUEST, 'message':FAIL}
            return result
        
    def logoutUser(request):
        """
        This method is used to logout authenticated user.
        """
        logout(request)
        result = {'code':HTTP_200_OK, 'message':OK}  
        return result      

    def getAllusers(request):
        """
        This method is used to retreive all users.
        """
        role = request.data.get('role',None)
        if role:
            users = User.objects.filter(role=role)
        else:
            users = User.objects.all()
        data = []
        for user in users:
            id = user.id
            email = user.email
            first_name = user.first_name
            last_name = user.last_name
            role = user.role.name
            data.append({
                'id':id, 'email':email,'first_name':first_name,
                'last_name':last_name,'role':role
            })
        return data


        
            
            

        
