from django.shortcuts import render

# Create your views here.
def ChanaChallenge(request):
    return render (request, 'InformacionEvento/chanachallenge.html')