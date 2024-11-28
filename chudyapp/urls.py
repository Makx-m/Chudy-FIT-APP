from django.urls import path
from chudyapp.views import index, indexPersons, indexPersonsJSON

urlpatterns = [
    path('test/', index),
    path('html/', indexPersons),
    path('persons/', indexPersonsJSON)
]