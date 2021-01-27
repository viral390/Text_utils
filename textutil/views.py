from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html")
    # return HttpResponse("hello")

def analyze(request):
    djtext = request.GET.get("text",'off')
    analyzed = ""
    punctuations = '''!()-{}'"[]:;/?<>,.@#$%^&*~'''
    for char in djtext:
        if char  not in punctuations:
            analyzed = analyzed + char
    param={'purpose':'removed punctuations','analyzed_text': analyzed}

    return render(request,'analyze.html',param)



#use diiferent way
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("new line remove")
#
# def spaceremover(request):
#     return HttpResponse("space remover <a href='/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("char count")
