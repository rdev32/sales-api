from django.urls import path
from costumers.views import RegisterView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
]
