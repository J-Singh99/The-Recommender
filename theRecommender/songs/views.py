from django.shortcuts import render
import joblib
import pandas
import Recommenders as Recommenders

# Create your views here.

#Returns the popular song (basically the default page)
def song(request): 
    popular           = joblib.load("popularityModel.sav")
    popular_song_list = popular.recommend("4bd88bfb25263a75bbdd467e74018f4ae570e5df")["song"].tolist()
    final_song_list=[]
    for song in popular_song_list:
        temp = song.split('-')
        final_song_list.append(temp)
   
    return render(request,'song.html',{'final_song_list':final_song_list })

#def get_popular_song(request):
    
     