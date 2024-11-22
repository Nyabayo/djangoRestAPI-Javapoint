from rest_framework import serializers
from .models import Students

class StudentSerializer(serializers.ModelSerializer):
    # Fields should be readable and writable (not just write-only unless necessary)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    address = serializers.CharField()
    roll_number = serializers.CharField()
    mobile_number = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new 'Student' instance given the validated data.
        """
        return Students.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Students' instance given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.address = validated_data.get('address', instance.address)
        instance.roll_number = validated_data.get('roll_number', instance.roll_number)
        instance.mobile_number = validated_data.get('mobile_number', instance.mobile_number)

        instance.save()
        return instance

    class Meta:
        model = Students  # This specifies the model associated with this serializer
        fields = '__all__'  # Include all fields from the 'Students' model
