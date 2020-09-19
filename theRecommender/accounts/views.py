from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html' , {'page':'index'} )

def chat(request):
    return render(request, 'chat.html' , {'page':'chat'} )