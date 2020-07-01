from rest_framework import serializers
from restindbank.models import Branches


class IndianBanksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branches
        fields = ('ifsc', 'bank', 'branch', 'address', 'city', 'district', 'state')
