from restindbank.api.viewsets import BankViewSets, BranchesViewSets, BankBranchesViewSets
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('bank', BankViewSets)
routers.register('branches', BranchesViewSets)
routers.register('bankbranches', BankBranchesViewSets)

