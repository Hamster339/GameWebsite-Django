from django.contrib.auth.models import User 
from django import forms
from gamewebsite.models import UserProfile, Languages, TimeZones, MatchRequests, Game
from django.forms import inlineformset_factory

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta: 
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm): 
    class Meta:
        model = UserProfile
        fields = ('contactInfo',)

class RequestForm(forms.ModelForm):

    # the user making the request
    user = forms.ModelChoiceField(widget=forms.HiddenInput,queryset=User.objects.all())
    # the name of the current game (the current page)
    game = forms.ModelChoiceField(widget=forms.HiddenInput,queryset=Game.objects.all())

    # one of the languages from the language model
    language = forms.ModelChoiceField(queryset=Languages.objects.all(), empty_label=None, label="Language to play in")
    
    # the timezone the user wishes to play in
    time = forms.DateTimeField(label="Time to play at ( MM/DD/YY HH:MM)")
    
    # the number of players the user wishes to play with
    capacity = forms.IntegerField(min_value=1, label="Number of people to play with")
    
    class Meta:
        model = MatchRequests
        fields = ['user', 'game', 'language', 'time', 'capacity']
     
