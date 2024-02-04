# Create your views here.
# request -> response
# request handler (action, called view in Django, while views are called template in Django)

from django.shortcuts import render
from django.http import HttpResponse


# these functions ...
#  - Pull data from db
#  - Transform
#  - send email etc.

def say_hello(request):
    return render(request, 'hello.html', )