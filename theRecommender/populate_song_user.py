import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'theRecommender.settings')
import django
django.setup()
from accounts.models import User
from songs.models import songInfo
import random

if __name__ == '__main__':
    user = User.objects.get(username='Malvika')
    print(user)
    print("Starting...")
    
    songs = {"Just Lose It - Eminem",
             "Without Me - Eminem",
             "16 Candles - The Crests",
             "Speechless - Lady GaGa",
             "Push It - Salt-N-Pepa",
             "Ghosts 'n' Stuff(Original Instrumental Mix) - Deadmau5",
             "Say My Name - Destiny's Child",
             "My Dad's Gone Crazy - Eminem / Hailie Jade",
             "The Real Slim Shady - Eminem",
             "Somebody To Love - Justin Bieber"}

    songs2 = {"Swallowed In The Sea - Coldplay",
             "Life In Technicolor ii - Coldplay",
             "Life In Technicolor - Coldplay",
             "The Scientist - Coldplay",
             "Trouble - Coldplay",
             "Strawberry Swing - Coldplay",
             "Lost! - Coldplay",
             "Clocks - Coldplay"}

    for i in songs2:
        song = songInfo.objects.create(user_id=user, song=i, listen_count= random.randint(1,5))
        song.save()
