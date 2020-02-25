from rest_framework import serializers
from baserooter.models import deploymentRequest

class requestDeploySerializer(serializers.ModelSerializer):
    class Meta:
        model = deploymentRequest
        fields = ('id','program_version','requested_branch','requested_by','description','technician_id','status')

    
        
    
    



