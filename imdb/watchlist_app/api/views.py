from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework  import status
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib.auth.models import User
from .serializer import RegistrationSerializers

@api_view(['POST',])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
