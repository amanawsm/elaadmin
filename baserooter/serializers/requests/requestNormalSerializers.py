from rest_framework import serializers
from baserooter.models import requestNormal

class requestNormalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = requestNormal
        fields = ('id','title','description','attachment','status','requested_by','created_at')
    
    



