from baserooter.models import Environment
from baserooter.serializers import environmentSerializer
from baserooter.utils import *
from rest_framework.status import *

class environmentService():
    def getEnvironments(request):
        """
        This method is used to retreive all environments.
        """
        environments = Environment.objects.all()
        serializer = environmentSerializer(environments, many=True)
        result = {'data':serializer.data, 'code':HTTP_200_OK, 'message':OK}
        return result