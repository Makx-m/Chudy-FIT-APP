import json
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jwt
from django.conf import settings
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from chudyapp.models.PersonModel import Person
from django.core import serializers

# JWT Secret key and expiration time
SECRET_KEY = settings.SECRET_KEY
EXPIRATION_TIME = timedelta(days=1)

def index(request):
    return HttpResponse("test")

def indexPersons(request):
    persons = Person.objects.all()
    persons = persons[:100] # limit do 100 osob
    return render(request, template_name='persons.html', context={
        'persons': persons
    })


def indexPersonsJSON(request):
    persons = Person.objects.all()
    persons = persons[:100]
    data = serializers.serialize(format='json', queryset=persons)
    return HttpResponse(data, content_type="*application/json")


def generate_jwt(user):
    payload = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + EXPIRATION_TIME,
        'iat': datetime.utcnow(),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  
            username = data.get("username")
            password = data.get("password")
            print(username)
            print(password)
            user = authenticate(username=username, password=password)

            if user is not None:
                jwt_token = generate_jwt(user)
                return JsonResponse({"message": "success", "user": {"username": user.username, "jwt": jwt_token}}, status=200)
            else:
                return JsonResponse({"message": "Incorrect username or password"}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)
    return JsonResponse({"message": "Invalid method"}, status=405)
@csrf_exempt
def signup_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                return JsonResponse({"message": "Username and password are required"}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({"message": "User already exists"}, status=400)

            user = User.objects.create_user(username=username, password=password)
            return JsonResponse({"message": "User created successfully", "user": {"username": user.username}}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)
    return JsonResponse({"message": "Invalid method"}, status=405)

@csrf_exempt
def change_password(request):
    
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data)
            # data = json.loads(request.body)
            username = data.get("username")
            new_password = data.get("new_password")
            password = data.get("password")
           
            if not username or not new_password:
                return JsonResponse({"message": "Username and new_password are required"}, status=400)

            try:
                # user = User.objects.get(username=username, password=password)
                user = authenticate(username=username, password=password)
            except User.DoesNotExist:
                return JsonResponse({"message": "User not found"}, status=404)

            user.set_password(new_password)
            user.save()

            return JsonResponse({"message": "Password updated successfully"}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON format"}, status=400)
    return JsonResponse({"message": "Invalid method. Use POST."}, status=405)


from django.urls import path
from chudyapp.views import index, indexPersons, indexPersonsJSON, login_view, signup_view
from .views import change_password 
