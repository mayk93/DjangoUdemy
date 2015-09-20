from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('This is the polls application.')

def detail(request,questionID):
    return HttpResponse('Question ID: ' + str(questionID))

def results(request,questionID):
    return HttpResponse('Results for queston: ' + str(questionID))

def vote(request,questionID):
    return HttpResponse('Vote for queston: ' + str(questionID))
