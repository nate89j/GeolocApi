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

For testing:
send a post request via postman to http://127.0.0.1:8000/api/token/ with body: {"username": "username", "password": "password"} and we expect to see the output like this:
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNDQ1NzEwOCwianRpIjoiMzExODY5NWI1MjIxNDkwNDllYTIyMDc1MDVhYmJmMzAiLCJ1c2VyX2lkIjoyfQ.6dtje7bF6-rB3UljRiYzNFZIAq7Yhdq9zp2Ruff-bp8",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE0MzcxMDA4LCJqdGkiOiIxMzA3OTJkNDBkZWE0N2ZmYjgwZGRjNjdmNTBjYTZjYyIsInVzZXJfaWQiOjJ9.ukY1NHgIoafcpC2Aw0lvPXSyP-MX49LSnG66xSKkeIQ"
}


**DJANGO API**

