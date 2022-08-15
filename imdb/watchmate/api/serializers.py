from rest_framework import serializers
from watchmate.models import Movie

"""
field level validation
"""
def validator_name(value):
    if len(value) < 2 :
        raise serializers.ValidationError("name length most be greater than two")

class MovieSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validator=[validator_name])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.description = validate_data.get('description', instance.description)
        instance.active = validate_data.get('active', instance.active)
        instance.save()
        return instance

    """
    object level validation
    """
    def validate(self , data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description must not be same')
        return data
