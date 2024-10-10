from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json

global user_access_level

def index(request):
    return JsonResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def login_user(request):
    global user_access_level
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(request, username=data.get('usernameField'), password=data.get('passwordField'))
        if user is not None:
            user_access_level = user.access_level
            return JsonResponse({'access_level': user_access_level})
        else:
            return JsonResponse({'message':'User dont have login'})

@csrf_exempt
def digital_authentication(request):
    global user_access_level
    if request.method == 'GET':
        return JsonResponse({'access_level': user_access_level})
    
@csrf_exempt
def facial_authentication(request):
    if request.method == 'GET':
        return JsonResponse({'message':'Teste'})