from baserooter.models import Program,programVersion,Application
from baserooter.serializers import programSerializer
from baserooter.utils import *
from rest_framework.status import *


class applicationsViewServices():

    def getApplicationType(request):
        """
        This method is used to retreive all application types.
        """
        env_id = request.data.get('environment',None)
        if env_id:
            programs_instance = Program.objects.filter(environment_id = env_id)
            if len(programs_instance)==0:
                result = {'code':HTTP_204_NO_CONTENT, 'message':RECORD_NOT_FOUND}
            else:                   
                data = []
                app_type = []                
                for instance in programs_instance:
                    app_type_id = instance.application_type.id
                    app_type_name = instance.application_type.name
                    env_id = instance.environment.id
                    env_name = instance.environment.name
                    if app_type_id not in app_type:
                        app_type.append(app_type_id)
                        data.append({'id':app_type_id,'name':app_type_name})
                    else:
                        pass
                result = {'data':sorted(data, key = lambda i: i['id']), 'code':HTTP_200_OK, 'message':OK}
        else:
            result = {'code':HTTP_400_BAD_REQUEST, 'message':DETAILS_INCORRECT}
        return result

    def getApplications(request):
        """
        This method is used to retreive all applications along with program versions.
        """
        env_id = request.data.get('environment',None)
        app_type_id = request.data.get('app_type_id',None)
        if env_id and app_type_id:
            version_instance = programVersion.objects.filter(application__program__environment=env_id, application__program__application_type=app_type_id)
            if len(version_instance) == 0:
                result = {'code':HTTP_204_NO_CONTENT, 'message':RECORD_NOT_FOUND}
            else:
                data = []
                server1 = []
                program_id1 = []
                app_type_id1 = []
                count = -1        
                for instance in version_instance:
                    version_id = instance.id
                    version = instance.name
                    app_id = instance.application.id
                    app_name = instance.application.name            
                    program_id = instance.application.program.id
                    program_name = instance.application.program.name
                    server = instance.application.program.server
                    app_type_id = instance.application.program.application_type.id
                    app_type_name = instance.application.program.application_type.name
                    d = {'version_id':version_id,'version':version}
                    if (server in server1) and (program_id in program_id1) and (app_type_id in app_type_id1):             
                        for apps_id in data[count]['applications']:
                            if app_id == apps_id['app_id']:
                                apps_id['version_id'] =version_id
                                apps_id['version'] =version
                    else:
                        server1.append(server) 
                        program_id1.append(program_id)
                        app_type_id1.append(app_type_id)
                        count += 1                
                        apps_instance = Application.objects.filter(program__environment=env_id,program__application_type=app_type_id,program=program_id)
                                
                        apps = []
                        for app_instance in apps_instance:
                            app_id2 = app_instance.id 
                            app_name2 = app_instance.name
                            e = {'app_id':app_id2,'app_name':app_name2,'version_id':'','version':''}
                            if app_id == app_id2:
                                e['version_id'] =version_id
                                e['version'] =version

                            apps.append(e)
                        final = {'server':server,'app_type_id':app_type_id,'app_type_name':app_type_name,
                                'program_id':program_id,'program_name':program_name,'applications':sorted(apps, key = lambda i: i['app_id'])}         
                        data.append(final)
                result = {'data':sorted(data, key = lambda i: i['program_id']), 'code':HTTP_200_OK, 'message':OK}

        else:
            result = {'code':HTTP_400_BAD_REQUEST, 'message':DETAILS_INCORRECT}
        return result
    

    
                
        
    
    




    