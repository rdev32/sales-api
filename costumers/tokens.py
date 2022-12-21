from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

logged_user = get_user_model()

def create_token(user: logged_user):
    token = RefreshToken.for_user(user)
    return {
        'access': str(token.access_token),
        'refresh': str(token),
    }