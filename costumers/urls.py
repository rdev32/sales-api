from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from costumers.views import RegisterView, ListCostumersView, LoginView
from rest_framework.routers import DefaultRouter
from django.urls import path

costumers_router = DefaultRouter()
costumers_router.register(r'costumers', ListCostumersView, basename='costumers')

urlpatterns = [
    path(r'login/', LoginView.as_view(), name='login'),
    path(r'register/', RegisterView.as_view(), name='register'),
    path(r'token/new/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(r'token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += costumers_router.urls