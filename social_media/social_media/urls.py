from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,)
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('post.urls')),
    path('user/', include('user_profile.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
