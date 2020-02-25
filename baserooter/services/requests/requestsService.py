from baserooter.serializers import requestDeploySerializer, requestNormalSerializer
from baserooter.models import  deploymentRequest,programVersion,requestNormal
from baserooter.utils import *
from rest_framework.status import *
from baserooter.utils import CustomPagination




class requestsService():

    def createNormalRequest(request):
        """
        This method is to create new normal requests.
        """
        title = request.data.get('title',None)
        desc = request.data.get('description',None)
        attachment = request.data.get('attachment',None)
        status_type = request.data.get('status',None)
        requested_by = request.data.get('requested_by',None)
        if title and desc and status_type and requested_by:
            serializer = requestNormalSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                result = {'data':serializer.data, 'code':HTTP_201_CREATED, 'message':OK}
            else:
                result = {'data':serializer.errors, 'code':HTTP_201_CREATED, 'message':OK}                
        else:
            result = {'code':HTTP_400_BAD_REQUEST, 'message':FAIL}
        return result
    def getNormalRequest(request):
        """
        This method is to retreive all normal requests.
        """
        search_keys = ['title__icontains','status__icontains','requested_by__icontains', 'id__contains']
        search_type = 'or'
                
        queryset = requestNormal.objects.all()
        if len(queryset) == 0:
            result = {'code':HTTP_204_NO_CONTENT, 'message':RECORD_NOT_FOUND}
        else:            
            serializer = requestNormalSerializer(queryset, many = True)
            data = CustomPagination.get_custom_pagination(request, requestNormal, search_keys, search_type, requestNormalSerializer, queryset)
            result = {'data':data['response_data'],'total_records':data['total_records'], 'code':HTTP_200_OK, 'message':OK}
        return result

    def updateNormalRequest(request):
        """
        This method is used to update status and program version.
        """
        normal_id = request.data.get('id',None)
        normal_status = request.data.get('status',None)
        if normal_id and normal_status:            
            normal_request = requestNormal.objects.get(id=normal_id)
            normal_request.status = normal_status
            normal_request.save()
            result = {'code':HTTP_200_OK, 'message':UPDATED}                
        else:
            result = {'code':HTTP_200_OK, 'message':DETAILS_INCORRECT}
        return result

    def createDeploymentRequest(request):
        """
        This method is used to create deployment requests.
        """        
        requested_branch = {}
        version_id = request.data.get('program_version')
        new_version = request.data.get('version')
        requested_by = request.data.get('requested_by')
        description = request.data.get('description')
        technician_id = request.data.get('technician_id')
        status_type = request.data.get('status')
        version_instance = programVersion.objects.get(id=int(version_id))
        old_version = version_instance.name
        app_id = version_instance.application.id
        program_id = version_instance.application.program.id
        app_type_id = version_instance.application.program.application_type.id
        env_id = version_instance.application.program.environment.id
        requested_branch.update({
            'env_id':env_id,'app_type_id':app_type_id,
            'program_id':program_id,'app_id':app_id,'version_id':version_id,
            'old_version':old_version, 'new_version':new_version
        })
        data = {'program_version':version_id,'requested_branch':str(requested_branch),'requested_by':requested_by,'description':description,'technician_id':technician_id,'status':status_type}
        serializer = requestDeploySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            result = {'data':serializer.data, 'code':HTTP_201_CREATED, 'message':OK}
        else:
            result = {'data':serializer.errors, 'code':HTTP_201_CREATED, 'message':OK}

        return result  

    def getDeploymentRequest(request):
        """
        This method is to retreive all deployment requests.
        """
        search_keys = ['description__icontains','status__icontains','requested_by__icontains', 'id__contains']
        search_type = 'or'
        queryset = deploymentRequest.objects.all()
        if len(queryset) ==0:
            result = {'code':HTTP_204_NO_CONTENT, 'message':RECORD_NOT_FOUND}
        else:
            serializer = requestDeploySerializer(queryset, many=True)
            data = CustomPagination.get_custom_pagination(request, deploymentRequest, search_keys, search_type, requestDeploySerializer, queryset)
            
            for data1 in data['response_data']:
                data1['requested_branch'] =eval(data1['requested_branch'])
              
            result = {'data':data['response_data'],'total_records':data['total_records'], 'code':HTTP_200_OK, 'message':OK}
        return result  
     
    def updateDeploymentRequest(request):
        """
        This method is used to update status and program version.
        """
        deployment_id = request.data.get('id',None)
        deployment_status = request.data.get('status',None)
        if deployment_id and deployment_status:
            if str(deployment_status).lower() == 'done':
                deployment = deploymentRequest.objects.get(id=deployment_id)
                new_version = eval(deployment.requested_branch)['new_version']
                version_id = eval(deployment.requested_branch)['version_id']
                old_version = eval(deployment.requested_branch)['old_version']
                program_version = programVersion.objects.get(id=version_id)
                print(program_version.name)
                program_version.name = str(new_version)
                program_version.save()
                deployment.status = deployment_status
                deployment.save()
                result = {'code':HTTP_200_OK, 'message':UPDATED +' to '+ str(new_version)}              
            else:
                deployment = deploymentRequest.objects.get(id=deployment_id)
                deployment.status = deployment_status
                deployment.save()
                result = {'code':HTTP_200_OK, 'message':UPDATED}                
        else:
            result = {'code':HTTP_200_OK, 'message':DETAILS_INCORRECT}
        return result
            