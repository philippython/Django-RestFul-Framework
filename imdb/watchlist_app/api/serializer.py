from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class RegistrationSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"},write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            "password" : {"write_only": True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password == password2:
            user = User.objects.filter(email=self.validated_data['email'])
            if user.exists():
                raise ValidationError({"error" : "User already exist"})
            else:
                account = User(username=self.validated_data['username'], email=self.validated_data['email'])
                account.set_password(password)

                account.save()

                return account
        else:
            raise ValidationError({"error" : "Password doesn't match password2"})
