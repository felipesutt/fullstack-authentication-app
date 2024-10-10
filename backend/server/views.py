from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        print(request)
