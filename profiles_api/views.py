#
from rest_framework.views import APIView
#Response object : return responses from the API view
from rest_framework.response import Response
#status from the api
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request,format=None):
        """"Returns a list of api view features"""

        an_apiview = [
            'Uses http methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your app logic',
            'Is mapped manually to URLs',
        ]
        #the dictionary needs to return a dictionary

        return Response({'message':'Hello', 'an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle updating an object"""
        serializer = self.serializer_class(data=request.data)
        #pk = primary key
        return Response({'method':'PUT'})


    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        #e.g. update only the last_name field
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
