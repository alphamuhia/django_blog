from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')

def about(request):
    context ={
        'message': 'Hello everyone, welcome to my blog'
    }
    return render(request, 'about.html', context)