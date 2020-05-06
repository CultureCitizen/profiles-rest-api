from rest_framework import serializers

#access our models
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our Api View"""
    #whenever you are making a put / post / patch , expect an input with name(length=10)
    name = serializers.CharField(max_length=10)


class UserProfilesSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    #metaclass for serialization
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }}

    #overwrite the serialization for the create method
    def create(self, validated_data):
        """Create and return a new user"""
        #call the function from our model which passes the hashed password
        #instead of passing it as plain text
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
