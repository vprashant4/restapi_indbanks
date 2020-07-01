from django.contrib import admin
from django.urls import path, include
from .router import routers
#from rest_framework.authtoken import views
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', include(routers.urls)),
    path('admin/', admin.site.urls),
    path('api/', include(routers.urls)),
    #path('api/token/', views.obtain_auth_token, name='token_obtain_pair'),

    # path('api-auth/', include('rest_framework.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
