# GeolocApi

**JWT Authentication:**

install:
pip install djangorestframework-simplejwt

add to settings.py
REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    ...
}

add to urls.py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]

You can also include a route for Simple JWT’s TokenVerifyView if you wish to allow API users to verify HMAC-signed tokens without having access to your signing key:

urlpatterns = [
    ...
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ...
]

