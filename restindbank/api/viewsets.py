from restindbank.models import Banks, Branches, BankBranches
from .serializers import BanksSerializer, BranchesSerializer, BankBranchesSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


class BankFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Banks
        fields = ['name']


class BranchesFilter(filters.FilterSet):

    class Meta:
        model = Branches
        fields = ['ifsc']


class BankBranchesFilter(filters.FilterSet):
    bank_name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = BankBranches
        fields = ['ifsc', 'city', 'bank_name']


class BankViewSets(viewsets.ModelViewSet):
    queryset = Banks.objects.all()
    serializer_class = BanksSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BankFilter


class BranchesViewSets(viewsets.ModelViewSet):
    queryset = Branches.objects.all().order_by('bank')
    serializer_class = BranchesSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BranchesFilter


class BankBranchesViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = BankBranches.objects.all().order_by('bank_id')
    serializer_class = BankBranchesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BankBranchesFilter