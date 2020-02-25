from rest_framework import serializers
from baserooter.models import applicationType

class applicationTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = applicationType
        fields = ('id','name',)