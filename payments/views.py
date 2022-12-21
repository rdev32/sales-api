from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from payments.models import Payment
from payments.serializers import PaymentSerializer
from payments.pagination import PaymentsSetPagination

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.get_queryset().order_by('date')
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    pagination_class = PaymentsSetPagination
    search_fields = ['usuario__id', 'fecha_pago', 'servicio']
    throttle_scope = 'payments'

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)