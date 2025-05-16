from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Welcome': 'Welcome to ALX Travel App API!',
        'Swagger': '/swagger/',
    }
    return Response(api_urls)