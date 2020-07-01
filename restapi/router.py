from restindbank.api.viewsets import RestIndBankViewSets
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('branches', RestIndBankViewSets)

