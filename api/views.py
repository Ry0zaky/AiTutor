from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to AiTutor API!"})
    
@api_view(['POST'])
def ask_ai(request):
    user_input = request.data.get("question")  # Get question from frontend
    fake_response = {"answer": "This is a placeholder response until the AI API is integrated."}
    return Response(fake_response)