from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html")
    # return HttpResponse("hello")

def analyze(request):
    djtext = request.POST.get("text",'default')
    rmpunc = request.POST.get('rmpunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover =request.POST.get('newlineremover','off')

    if rmpunc == "on":
        punctuations = '''!()-{}'"[]:;/?<>,.@#$%^&*~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        param={'purpose':'removed punctuations','analyzed_text': analyzed}

        return render(request,'analyze.html',param)


    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', param)


    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char.upper()
        param = {'purpose': 'remove new lines', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', param)



    else:
        return HttpResponse("Error")


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
