from django.urls import path
from . import views # so we can reference view functions

# URLConf module (URL configuration, every app has its own)
urlpatterns = [
    path('hello/', views.say_hello)
]