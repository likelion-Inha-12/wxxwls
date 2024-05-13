from django.http import HttpResponse
from rest_framework.response import Response

def health(request):
    return HttpResponse("Healthy!")

def api_response(data, message, status):
    response = {
        "message":message,
        "data":data
    }
    return Response(response, status=status)