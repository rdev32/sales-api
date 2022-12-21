from django.urls import path
from costumers.views import RegisterView, CostumersView, LoginView

urlpatterns = [
    path(r'register/', RegisterView.as_view(), name='register'),
    path(r'costumers/', CostumersView.as_view(), name='costumers'),
    path(r'login/', LoginView.as_view(), name='login'),
]