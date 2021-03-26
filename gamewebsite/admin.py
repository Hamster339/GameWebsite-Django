from django.contrib import admin

# Register your models here.
from gamewebsite.models import *

admin.site.register(TimeZones)
admin.site.register(Languages)
admin.site.register(Game)
admin.site.register(UserProfile)
admin.site.register(MatchRequests)
admin.site.register(AcceptedMatches)