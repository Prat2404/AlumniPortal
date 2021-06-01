from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'client/newsfeed.html')

def chat(request):
    return render(request,'client/message.html')