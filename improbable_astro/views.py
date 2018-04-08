from django.shortcuts import render 




def hello_world(request, x=None): # all views accept a request
    #return HttpResponse("<h1>Hello Cruel World</h1></br><h1>Coming soon MOVIES!!!!</h1>")
    return render(request, 'home.html')

