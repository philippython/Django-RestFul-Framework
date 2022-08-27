from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework  import status
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from  watchlist_app import models
from .serializer import RegistrationSerializers


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
            token = Token.objects.get(user=account).key
            data["token"] = token

            return Response(data)

        else:
            return Response(serializer.errors)
