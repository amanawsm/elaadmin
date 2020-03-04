from baserooter.serializers import requestDeploySerializer, requestNormalSerializer
from baserooter.models import  deploymentRequest,programVersion,requestNormal
from baserooter.utils import *
from rest_framework.status import *
from baserooter.utils import CustomPagination
from django.contrib.auth import get_user_model
User = get_user_model()



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
        data_len = request.data.get('data',None)
        print("data_len -> ",data_len)
        final_result = []
        for request_data in data_len:
            requested_branch = {}
            version_id = request_data['version_id']
            new_version = request_data['version']
            requested_by = request_data['requested_by']
            description = request_data['description']
            technician_id = request_data['technician_id']
            status_type = request_data['status']
            version_instance = programVersion.objects.get(id=int(version_id))
            old_version = version_instance.name
            app_id = version_instance.application.id
            app_name = version_instance.application.name
            program_id = version_instance.application.program.id
            program_name = version_instance.application.program.name
            app_type_id = version_instance.application.program.application_type.id
            app_type_name = version_instance.application.program.application_type.name
            env_id = version_instance.application.program.environment.id
            env_name = version_instance.application.program.environment.name
            
            requested_branch.update({
                'env_id':env_id,'env_name':env_name,'app_type_id':app_type_id,'app_type_name':app_type_name,
                'program_id':program_id,'program_name':program_name,'app_id':app_id,'app_name':app_name,'version_id':version_id,
                'old_version':old_version, 'new_version':new_version
            })
            data = {'program_version':version_id,'requested_branch':str(requested_branch),'requested_by':requested_by,'description':description,'technician_id':technician_id,'status':status_type}
            serializer = requestDeploySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                result = {'data':serializer.data, 'code':HTTP_201_CREATED, 'message':OK}
            else:
                result = {'data':serializer.errors, 'code':HTTP_201_CREATED, 'message':OK}
            final_result.append(result)

        return final_result  

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
                try:
                    tech_instance = User.objects.get(id=data1['technician_id'])
                    tech_first_name = str(tech_instance.first_name)
                    tech_role = tech_instance.role.name
                    tech_email = tech_instance.email
                    tech_details = {'id':data1['technician_id'],'name':tech_first_name,'email':tech_email,'role':tech_role}
                except:
                    tech_details = {'error':'technician details not exists'}
                data1['technician_id'] = tech_details
              
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
    def updateProgramVersion(request):
        env_name = request.data.get('env_name',None)
        app_type_name = request.data.get('app_type_name',None)
        program_name = request.data.get('program_name',None)
        app_name = request.data.get('app_name',None)
        version = request.data.get('version',None)
        
        if env_name and app_type_name and program_name and app_name and version:
            version_instance = programVersion.objects.filter(application__program__environment_name=env_name, application__program__application_type_name=app_type__name,application__program_name=program_name,application_name=app_name)
            print("version_instance : ",version_instance)
            version_id = version_instance[0].id
            print("version_id : ",version_id)
            program_version = programVersion.objects.get(id=version_id)
            print(program_version.name)
            program_version.name = str(version)
            program_version.save()

