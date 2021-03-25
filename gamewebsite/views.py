from django.shortcuts import render
from django.http import HttpResponse
from gamewebsite.models import Game

# displays games the user can choose from
def game_library(request):
#    context_dict = {}
    # return 4 most popular in descending order
    
    # return 4 best rated in descending order
    
    # return 4 newest in descending order
#    newest_games = Category.objetcs.order_by('-date_added')[:4]

#    context_dict['newest']= newest_games
    
    return render(request, 'gamewebsite/base.html') #, context= context_dict)
 
# the user can search for other users that fit their requirements
# def search_matches(request):
    # return render(request, 'gamewebsite/search_matches.html')

# the user can log in to their account
def log_in(request):
    return render(request, 'gamewebsite/log_in.html')

# the user can view their account details
def my_account(request):
    return render(request, "gamewebsite/my_account.html")

# the user can edit their account
def edit_account(request):
    return render(request, "gamewebsite/edit_account.html")
    
# displays information about a user selected game
# def game_page(request, game_name_slug):
    
    # return HttpResponse('game page')
    
def contact_us(request):
    return render(request, "gamewebsite/contact_us.html")

