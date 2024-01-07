from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def test(request):
    return render(request, 'test.html')

