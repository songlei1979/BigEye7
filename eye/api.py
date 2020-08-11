from eye.models import Client, Case, Payment, Investigator, Equipment, Assignment, Allocation
from rest_framework import viewsets, permissions
from .serializers import ClientSerializer, CaseSerializer, PaymentSerializer, InvestigatorSerializer, \
    EquipmentSerializer, AssignmentSerializer, AllocationSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClientSerializer

class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CaseSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PaymentSerializer

class InvestigatorViewSet(viewsets.ModelViewSet):
    queryset = Investigator.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = InvestigatorSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EquipmentSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AssignmentSerializer

class AllocationViewSet(viewsets.ModelViewSet):
    queryset = Allocation.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AllocationSerializer