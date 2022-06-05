from django.shortcuts import render

# Create your views here.
def indexx(request):
    return render(request,'indexx.html')

def first(request):
    return render(request,'first.html')

def second(request):
    return render(request,'second.html')

def third(request):
    return render(request,'third.html')