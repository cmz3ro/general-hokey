from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_app1(request):
    return render(request, 'index.html')

def dorojka(request):
    return render(request, 'dorojka.html')