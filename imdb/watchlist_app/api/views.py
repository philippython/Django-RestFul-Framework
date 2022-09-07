from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework  import status
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import RegistrationSerializers
# from  watchlist_app import models


@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({"response": "Logout successful "}, status=status.HTTP_202_ACCEPTED)

@api_view(['POST',])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializers(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data["response"] = "Registration Successful"
            data["username"] = account.username
            data["email"] = account.email

            def get_tokens_for_user(account):
                refresh = RefreshToken.for_user(account)
            
                data["JWT-token"] = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            get_tokens_for_user(account)
            return Response(data)

        else:
            return Response(serializer.errors)

    