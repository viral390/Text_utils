from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html")
    # return HttpResponse("hello")

def rmpunc(request):
    print(request.GET.get("text",'default'))
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("new line remove")

def spaceremover(request):
    return HttpResponse("space remover <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("char count")
