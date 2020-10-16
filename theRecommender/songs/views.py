from django.shortcuts import render

# Create your views here.
def song(request): 
    return render(request,'song.html' )
