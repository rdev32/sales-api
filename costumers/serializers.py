from rest_framework import serializers
from costumers.models import Costumer

class CostumerSerializer(serializers.ModelSerializer):
    class Meta():
        model = Costumer
        fields = ['id', 'username', 'email', 'password']