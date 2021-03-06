from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('main', views.main, name='main'),
    path('register', views.register, name='register'),
    path('viewother', views.viewother, name='viewother'),
    path('success', views.success, name='success'),
    # path('login', views.login, name='login'),
    path('welcome', views.welcome),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]