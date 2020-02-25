from rest_framework import serializers
from baserooter.models import Environment

class environmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Environment
        fields = ('id','name',)