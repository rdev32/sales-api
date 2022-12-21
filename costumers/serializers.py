from rest_framework import serializers
from costumers.models import Costumer

class CostumerSerializer(serializers.ModelSerializer):
    class Meta():
        model = Costumer
        fields = ['id', 'username', 'email', 'password']
        exra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance