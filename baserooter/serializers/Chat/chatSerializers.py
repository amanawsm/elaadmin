from rest_framework import serializers
from baserooter.models import chatModel


class chatSerializer(serializers.ModelSerializer):
    class Meta:
        model = chatModel
        fields = ('id','normal','deployment','message')