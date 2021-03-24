from django.shortcuts import render
from django.http import HttpResponse

def game_library(request):
    return render(request, 'gamewebsite/base.html')
 
def search_matches(request):
    return HttpResponse("search for matches")

def log_in(request):
    return HttpResponse("log in")

def my_account(request):
    return HttpResponse("my account")

def edit_account(request):
    return HttpResponse("edit account")

def contact_us(request):
    return HttpResponse("contact us")
