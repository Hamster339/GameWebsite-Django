from gamewebsite.models import Game
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm, UserProfileForm, RequestForm
from django.contrib.auth import authenticate, login 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# displays games the user can choose from
def game_library(request):
    context_dict = {}
    # return 4 most popular in descending order
    most_popular = Game.objects.order_by('searches')[:4]
    # return 4 newest in descending order
    newest_games = Game.objects.order_by('-date_added')[:4]

    context_dict['newest'] = newest_games
    context_dict['popular'] = most_popular
   
    return render(request, 'gamewebsite/game_library.html' , context= context_dict)
 
# the user can search for other users that fit their requirements
# def search_matches(request):
    # return render(request, 'gamewebsite/search_matches.html')

# displays results page for a user searching for a game
def search(request):

    query = request.GET.get("query")
    result = Game.objects.filter(name__icontains=query)

    context_dict = {"query": query, "result": result}
    return render(request, 'gamewebsite/search.html', context=context_dict)

# the user can log in to their account
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:     
            if user.is_active:
                login(request, user)
                return redirect(reverse('gamewebsite:my_account'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login.")
    else:
        return render(request, 'gamewebsite/log_in.html')
    
def edit_account(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user,
                                                                        'userprofiles') else UserProfile.objects.create(
        user=request.user)
    
    if request.method == "POST":
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userprofile.contact_info = userprofile_cd['contactInfo']
            user.save()
            userprofile.save()
        return HttpResponseRedirect('gamewebsite/my_account/')

# the user can view their account details
@login_required(login_url='gamewebsite/log_in/')
def my_account(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user,
                                                                        'userprofiles') else UserProfile.objects.create(
        user=request.user)
    return render(request,'gamewebsite/my_account.html',{'user':user,'userprofile':userprofile}, context_instance=RequestContext(request))
  
# displays information about a user selected game
# allows user to search for others to play the selected game with
def game_page(request, game_name_slug):
    context_dict = {}

    try:
        
        game = Game.objects.get(slug=game_name_slug)
     
        context_dict['game'] = game
        context_dict['thumbNail'] = game.thumbNail
    
    except: 
        context_dict['game'] = None
        
    # and the game exists!
    if request.user.is_authenticated:
        form = RequestForm()

        if request.method =='POST':

            data = request.POST.copy()
            data["user"] = User.objects.get(username=request.user.username)
            data["game"] = game


            form = RequestForm(data)
            if form.is_valid():
                form.save(commit=True)
                return HttpResponse("Request submitted. Go to my account to see matched players")
            else:
                print(form.errors)

        else:
            form = RequestForm()

        context_dict['form'] = form
    return render(request, "gamewebsite/game_page.html", context=context_dict)
    
def contact_us(request):
    return render(request, "gamewebsite/contact_us.html")


def sign_up(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'gamewebsite/sign_up.html',
                  context = {'user_form': user_form,
                             'registered': registered})
@login_required
def restricted(request):
    return HttpResponse("You are logged in.")

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('gamewebsite:game_library'))
