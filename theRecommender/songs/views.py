from django.shortcuts import render
import joblib
import pandas
import Recommenders as Recommenders
from .models import songInfo
from django.contrib.auth.models import auth
import os 
from django.conf import settings
# Create your views here.
global unique
unique = joblib.load("itemModel.sav")
#Returns the popular song (basically the default page)
def song(request): 
    #****************first is popular list**********
    popular           = joblib.load("popularityModel.sav")
    popular_song_data = popular.recommend("4bd88bfb25263a75bbdd467e74018f4ae570e5df")
    popular_song_list = popular_song_data["song"].tolist()
    artist_list       = popular_song_data["artist_name"].tolist()
    release_list      = popular_song_data["release"].tolist()
    final_song_list=[]
    for i in range(len(popular_song_list)):
        song_info = popular_song_list[i].split('-') #
        song_info.append(artist_list[i])
        song_info.append(release_list[i])
        song_info.append(popular_song_list[i])
        final_song_list.append(song_info)
    #*************next is unique area**************
    
    all_unique_songs = songInfo.objects.filter(user_id=request.user).values_list('song', flat=True)
    unique_song_df   = unique.recommend(all_unique_songs)
    unique_song_list = unique_song_df["song"].tolist()
    final_song_list2 = []
    for i in range(len(unique_song_list)):
        song_info2 = unique_song_list[i].split('-')
        final_song_list2.append(song_info2)
    return render(request, 'song.html', {'page': 'songs','final_song_list': final_song_list, 'final_song_list2': final_song_list2})


def relatedSongs(request):
    #***********************this is only the current song
    #file = os.path.join(settings.BASE_DIR, 'itemModel.sav')
    song_title = request.GET.get("song_title")
    print(song_title)
    artist = request.GET.get("artist")
    print(artist)
    song_info  = []
    song_info.append(song_title)
    song_info.append(artist)
    #*************************this is the whole fukin list 
    song_similar     = song_title+"-"+artist
    print(song_similar)
    unique_song_df   = unique.get_similar_items([song_similar])
    unique_song_list = unique_song_df["song"].tolist()
    final_song_list2 = []
    for i in range(len(unique_song_list)):
        song_info2 = unique_song_list[i].split('-')
        final_song_list2.append(song_info2)
    return render(request, 'song2.html', {'page': 'songs', 'song_info': song_info, 'final_song_list2': final_song_list2})
    #is_model.get_similar_items(['U Smile - Justin Bieber'])

     
