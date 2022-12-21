from rest_framework import serializers
from rest_framework.authtoken.models import Token
from costumers.models import Costumer

class CostumerSerializer(serializers.ModelSerializer):
    class Meta():
        model = Costumer
        fields = ['id', 'username', 'email', 'password']
        exra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)

        if password is not None:
            user.set_password(password)
            user.save()
            Token.objects.create(user=user)
            return user
    
    def validate(self, attrs):
        username_exists = Costumer.objects.filter(username=attrs['username']).exists()
        if username_exists:
            raise serializers.ValidationError({'username': 'Username already exists'})
        return super().validate(attrs)

class RetrieveCostumerSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta():
        model = Costumer
        fields = ['id', 'username', 'password', 'email']