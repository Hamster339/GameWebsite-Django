import os
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WAD2_GameWebsite.settings')

import django
django.setup()
from gamewebsite.models import *


def populate():
    timezones = [{"timezone": "UTC-11"},
                 {"timezone": "UTC-10"},
                 {"timezone": "UTC-9"},
                 {"timezone": "UTC-8"},
                 {"timezone": "UTC-7"},
                 {"timezone": "UTC-6"},
                 {"timezone": "UTC-5"},
                 {"timezone": "UTC-4"},
                 {"timezone": "UTC-3"},
                 {"timezone": "UTC-2"},
                 {"timezone": "UTC-1"},
                 {"timezone": "UTC+0"},
                 {"timezone": "UTC+1"},
                 {"timezone": "UTC+2"},
                 {"timezone": "UTC+3"},
                 {"timezone": "UTC+4"},
                 {"timezone": "UTC+5"},
                 {"timezone": "UTC+6"},
                 {"timezone": "UTC+7"},
                 {"timezone": "UTC+8"},
                 {"timezone": "UTC+9"},
                 {"timezone": "UTC+10"},
                 {"timezone": "UTC+11"}]

    languages = [{"language": "English"},
                 {"language": "French"},
                 {"language": "Spanish"}]

    games = [{"name": "CS-GO", "description": "a shooty game", "date_added": datetime.datetime(2020, 5, 17, 12, 2, 3)},
             {"name": "Animal Crossing", "description": "gamey game", "date_added": datetime.datetime(2019, 5, 17, 11, 2, 3)}]

    for i in timezones:
        t = TimeZones.objects.get_or_create(timeZone=i["timezone"])[0]
        t.save()

    for i in languages:
        l = Languages.objects.get_or_create(language=i["language"])[0]
        l.save()

    for i in games:
        g = Game.objects.get_or_create(name=i["name"], description=i["description"], date_added=i["date_added"])[0]
        g.save()


if __name__ == "__main__":
    print("Starting Population Script...")
    populate()
    print("database populated")
