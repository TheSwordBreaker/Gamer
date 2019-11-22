from django.shortcuts import render
from review.models import rating

# Create your views here.

def homeView(request):
    return render(request,'home.html')

def gamesView(request):
    return render(request,'games.html')

def blogView(request):
    return render(request,'blog.html')

def forumView(request):
    return render(request,'forum.html')

def contactView(request):
    return render(request,'contact.html')
