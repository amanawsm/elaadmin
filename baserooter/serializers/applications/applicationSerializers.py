from rest_framework import serializers
from baserooter.models import Application

class applicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ('id','name','application_type','program')