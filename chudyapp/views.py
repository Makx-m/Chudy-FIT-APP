from django.shortcuts import render
from django.http import HttpResponse
from chudyapp.models.PersonModel import Person
from django.core import serializers

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