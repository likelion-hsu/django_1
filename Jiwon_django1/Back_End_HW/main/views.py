from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html',)

def first(request):
    return render(request,'main/first.html',)

def second(request):
    return render(request,'main/second.html',)

def third(request):
    return render(request,'main/third.html',)
