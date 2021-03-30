from django.contrib import admin
from gamewebsite.models import *
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(TimeZones)
admin.site.register(Languages)
admin.site.register(UserProfile)
admin.site.register(MatchRequests)
admin.site.register(AcceptedMatches)
admin.site.register(Game, GameAdmin)

