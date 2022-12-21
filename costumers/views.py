from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status

from costumers.serializers import CostumerSerializer, RetrieveCostumerSerializer
from .tokens import create_token
from costumers.models import Costumer

class RegisterView(APIView):
    serializer_class = CostumerSerializer

    def post(self, request):
        serializer = CostumerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
            }, status=status.HTTP_201_CREATED)

        return Response({
            'status': False,
            'data': serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)

class ListCostumersView(ReadOnlyModelViewSet):
    serializer_class = RetrieveCostumerSerializer
    queryset = Costumer.objects.all()

class LoginView(APIView):
    def get(self, request):
        return Response({
            'status': True,
            'data': {
                'user': str(request.username),
                'token': str(request.auth),
            }
        }, status=status.HTTP_200_OK)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({
                'status': False,
                'data': 'Username or password is missing.'
            }, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user.check_password(password):
            return Response({
                'status': False,
                'data': 'Incorrect credentials.'
            }, status=status.HTTP_404_NOT_FOUND)

        token = create_token(user)

        return Response({
            'status': True,
            'data': token
        }, status=status.HTTP_200_OK)
