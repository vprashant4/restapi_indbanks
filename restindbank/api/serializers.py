from rest_framework import serializers
from restindbank.models import Banks, Branches, BankBranches


class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = ('id', 'name')


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ('ifsc', 'bank', 'branch', 'address', 'city', 'district', 'state')
        depth = 1


class BankBranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankBranches
        fields = ('ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state', 'bank_name')