from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("this works")


def february(request):
    return HttpResponse("February")


def monthlyChallenge(request, month):
    # this 'month' needs to be matched with the one mentioned under dynamic binding.
    challengeText = None
    if (month == 'january'):
        challengeText = 'january'

    elif (month == 'february'):
        challengeText = 'february'

    elif (month == 'march'):
        challengeText = 'march'

    elif (month == 'april'):
        challengeText = 'april'

    else:
        return HttpResponseNotFound('Resource not found')
    return HttpResponse(challengeText)
