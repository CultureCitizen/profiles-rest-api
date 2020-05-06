from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our Api View"""
    #whenever you are making a put / post / patch , expect an input with name(length=10)
    name = serializers.CharField(max_length=10)
