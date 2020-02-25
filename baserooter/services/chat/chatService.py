from baserooter.models import chatModel
from baserooter.serializers import chatSerializer
from baserooter.utils import *
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST

class chatServices():

    def getChatLogs(request):
        normal_id = request.data.get('normal_id',None)
        deployment_id = request.data.get('deployment_id',None)
        if normal_id:
            queryset = chatModel.objects.filter(normal=normal_id)
            print(len(queryset))
            serializer = chatSerializer(queryset, many=True)            
            data = serializer.data             
            result = {'data':data, 'code':HTTP_200_OK, 'message':OK}
        elif deployment_id:
            queryset = chatModel.objects.filter(deployment=deployment_id)
            serializer = chatSerializer(queryset, many=True)
            data = serializer.data
            del data['normal']           
            result = {'data':data, 'code':HTTP_200_OK, 'message':OK}
        else:
            data = {'error':'please use valid parameters'}
            result = {'data':data, 'code':HTTP_400_BAD_REQUEST, 'message':FAIL}
         
        return result

    def createChatLogs(request):
        normal_id = request.data.get('normal_id',None)
        deployment_id = request.data.get('deployment_id',None)
        message = request.data.get('message',None)
        if normal_id:
            if message:
                request_data = {'normal':normal_id,'message':message}
                serializer = chatSerializer(data=request_data)
                if serializer.is_valid():
                    serializer.save()
                    data = serializer.data
                    del data['deployment'] 
                else:
                    data = serializer.errors
                result = {'data':data, 'code':HTTP_200_OK, 'message':OK}
        elif deployment_id:
            if message:
                request_data = {'deployment':deployment_id,'message':message}
                serializer = chatSerializer(data=request_data)
                if serializer.is_valid():
                    serializer.save()
                    data = serializer.data
                    del data['normal']
                else:
                    data = serializer.errors
                result = {'data':data, 'code':HTTP_200_OK, 'message':OK}
        else:
            data = {'error':'please use valid parameters'}
            result = {'data':data, 'code':HTTP_400_BAD_REQUEST, 'message':FAIL}
        
        return result