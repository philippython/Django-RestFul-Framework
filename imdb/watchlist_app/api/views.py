from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import Status
from rest_framework.error import ValidationError
from django.contrib.auth.models import User
from .serializers import RegistrationSerializers

@api_view(['POST',])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializers(request.data)
        if serializer.is_valid():
            user = User.objects.filter(email=request.data['email'])
            if user:
                raise ValidationError({"error" : "User already exist"})
            else:
                serializer.save()
                return Response(serializer.data, status=200)
        return Response(serializer.error, status=400)
