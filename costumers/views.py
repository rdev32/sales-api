from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from costumers.serializers import CostumerSerializer
from costumers.models import Costumer

class RegisterView(APIView):
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

class CostumersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        costumers = Costumer.objects.all()
        serializer = CostumerSerializer(costumers, many=True)
        return Response({
            'status': True,
            'data': serializer.data,
        })

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({
                'status': False,
                'data': 'Username or password is missing.'
            }, status=status.HTTP_400_BAD_REQUEST)

        user = Costumer.objects.filter(username=username).first()

        if not user.check_password(password):
            return Response({
                'status': False,
                'data': 'Incorrect credentials.'
            }, status=status.HTTP_404_NOT_FOUND)

        token = RefreshToken.for_user(user)

        return Response({
            'status': True,
            'data': {
                'refresh': str(token),
                'access': str(token.access_token),
            }
        }, status=status.HTTP_200_OK)
