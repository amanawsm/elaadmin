from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your serializers here
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username=validated_data['email']
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        print("validated_data : ",validated_data)
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(userSerializer, self).update(instance, validated_data)