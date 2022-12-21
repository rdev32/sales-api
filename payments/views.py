# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.generics import GenericAPIView
# from rest_framework.permissions import AllowAny

# from payments.serializers import SignUpSerializer, LoginSerializer

# class SignUpView(GenericAPIView):
#     serializer_class = SignUpSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class LoginView(APIView):
#     permission_classes = (AllowAny,)

#     def get(self, request):
#         return Response({'message': 'Hello, world!'})

#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
