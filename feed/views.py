from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'feed/home.html')

def chat(request):
    return render(request,'feed/chat.html')


def friends(request):
    return render(request,'feed/friends.html')