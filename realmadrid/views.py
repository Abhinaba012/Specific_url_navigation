from django.shortcuts import render

# Create your views here.

def real(request):
    return render(request, 'real.html')