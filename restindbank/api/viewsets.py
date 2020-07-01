from restindbank.models import Branches
from .serializers import IndianBanksSerializer
from rest_framework import viewsets
#from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


class RestIndBankFilter(filters.FilterSet):
    branch = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Branches
        fields = ['branch', 'ifsc', 'city']


class RestIndBankViewSets(viewsets.ModelViewSet):
    queryset = Branches.objects.all().order_by('ifsc')
    serializer_class = IndianBanksSerializer
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RestIndBankFilter
