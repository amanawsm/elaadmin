from rest_framework import serializers
from baserooter.models import Program

class programSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = ('id','name','server','environment','application_type')