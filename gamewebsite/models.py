from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Represents a timezone in format "UTC+/-x"
class TimeZones(models.Model):
    timeZone = models.CharField(max_length=128, unique=True)


# All languages available for users to speak
class AcceptedLanguages(models.Model):
    language = models.CharField(max_length=128)


# Represents user profiles
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profilePicture = models.ImageField(upload_to="media/profile_pictures", blank=True)
    contactInfo = models.CharField(max_length=128)
    timeZone = models.ForeignKey(TimeZones, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# Links users and AcceptedLanguages with many to many relationship
class UserHasLanguage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(AcceptedLanguages, on_delete=models.CASCADE)


# Represents a game
class Game(models.Model):
    name = models.CharField(max_length=128, unique=True)
    thumbNail = models.ImageField(upload_to="media/game_thumbnails", blank=True)
    description = models.CharField(max_length=128)
    date_added = models.DateField()

    def __str__(self):
        return self.name


# Represents a user's request for a match on a particular game
class MatchRequests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    language = models.ForeignKey(AcceptedLanguages, on_delete=models.CASCADE)
    time = models.TimeField(blank=True)

    def __str__(self):
        return "{" \
               + self.user.username \
               + "," + self.game.name \
               + "," + self.language.language \
               + "," + self.time.__str__() \
               + "}"


# Represents two users that have been matched
class AcceptedMatches(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{" + self.user1.username + "," + self.user2.username + "}"
