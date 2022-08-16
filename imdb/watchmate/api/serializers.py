from rest_framework import serializers
from watchmate.models import Movie



class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
    

    def validate(self , data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description must not be same')
        return data
    
    def validate_name(self, value):
        if len(value) < 2 :
            raise serializers.ValidationError("name length most be greater than two")
        return value
    
"""
field level validation

def validator_name(value):
    if len(value) < 2 :
        raise serializers.ValidationError("name length most be greater than two")

class MovieSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[validator_name])
    description = serializers.CharField()
    active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.description = validate_data.get('description', instance.description)
        instance.active = validate_data.get('active', instance.active)
        instance.save()
        return instance

   
    object level validation
  
    def validate(self , data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description must not be same')
        return data
"""