from django.http import HttpResponse



def hello_world(request): # all views accept a request
    return HttpResponse("<h1>Hello Cruel World</h1></br><h1>Coming soon MOVIES!!!!</h1>")

