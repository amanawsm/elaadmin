from rest_framework import serializers
from baserooter.models import programVersion

class programVersionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = programVersion
        fields = ('id','name','application','environment')