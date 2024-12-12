from django.urls import path
from chudyapp.views import index, indexPersons, indexPersonsJSON, login_view, signup_view
from .views import change_password
urlpatterns = [
    path('test/', index),
    path('html/', indexPersons),
    path('persons/', indexPersonsJSON),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('change_password/', change_password, name='change_password'),  
]



