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
    
    # def __init__(self, *args,**kwargs):
        # self.current_user = kwargs.pop('user')
        # self.game_name = kwargs.pop('game')
        # super(RequestForm, self).__init__(*args, **kwargs)
        
    
    # the user making the request
    user = forms.CharField(widget=forms.HiddenInput) #, initial = User.objects.get(username=self.current_user).username)
    # the name of the current game (the current page)
    game = forms.CharField(widget=forms.HiddenInput) #, initial = Game.objects.get(name=self.game_name).name)
    # pass in the user making the request and the game being searched
    def __init__(self, *args,**kwargs):
        self.user = kwargs.pop('user')
        super(RequestForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = User.objects.get(username=self.current_user).username
    one of the languages from the language model
    language = forms.ModelChoiceField(queryset=Languages.objects.all(), empty_label=None)
    
    # # the timezone the user wishes to play in
    timeZone = forms.ModelChoiceField(queryset=TimeZones.objects.all(), empty_label = None)
    
    # # the number of players the user wishes to play with
    capacity = forms.IntegerField(min_value=1)
    
    class Meta:
        model = MatchRequests
        fields = [ 'user','game','language', 'timeZone', 'capacity']
     
