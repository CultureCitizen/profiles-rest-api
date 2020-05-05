#
from rest_framework.views import APIView
#Response object : return responses from the API view
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""


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

        
