from rest_framework.routers import DefaultRouter
from payments.views import PaymentViewSet

payments_router = DefaultRouter()
payments_router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = payments_router.urls