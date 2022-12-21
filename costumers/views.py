from rest_framework.views import APIView
from costumers.serializers import CostumerSerializer
from rest_framework.response import Response
from rest_framework import status

class RegisterView(APIView):
    def post(self, request):
        serializer = CostumerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
            }, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'error',
            'message': serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)
