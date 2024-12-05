from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from chudyapp.models.PersonModel import Person
from django.core import serializers
import json

# Create your views here.
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

def login_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  
            username = data.get("username")
            password = data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                return JsonResponse({"message": "success", "user": {"username": user.username}}, status=200)
            else:
                return JsonResponse({"message": "Incorrect username or password"}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)
    return JsonResponse({"message": "Invalid method"}, status=405)

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