from django.http import HttpResponse



def hello_world(request): # all views accept a request
    return HttpResponse("Hello Cruel World")