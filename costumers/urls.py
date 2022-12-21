from django.urls import path
from costumers.views import RegisterView, CostumersView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path(r'register/', RegisterView.as_view(), name='register'),
    path(r'costumers/', CostumersView.as_view(), name='costumers'),
    path(r'login/', LoginView.as_view(), name='login'),
    path(r'login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]