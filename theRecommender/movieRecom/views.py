from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
import urllib.request, json 
from .models import links, Ratings
from .modelfunctions import allmovies, anger, anticipation, confusing, depressing, sad, excited, happy, inspring, thrilling,  getmovies

def movies(request):
    user_ratings = Ratings.objects.filter(user=request.user).values('movieid')
    user_items   = [ i['movieid'] for i in user_ratings]
    all_movies   = allmovies(user_items, request.user.id)
    pastwatch    = Ratings.objects.filter(user=request.user).order_by('-timestamp').values('movieid')
    pastwatch   = [ i['movieid'] for i in pastwatch]
    pastwatch   = getmovies(pastwatch)[:10]
    angermovies  = anger(user_items, request.user.id)
    #Anticipationmovie = anticipation(user_items, request.user.id)
    #confusingmovies = confusing(user_items, request.user.id)
    #Depressingmovie = depressing(user_items, request.user.id)
    #Sadmovie = sad(user_items, request.user.id)
    #Excitedmovie = excited(user_items, request.user.id)
    #Happymovie = happy(user_items, request.user.id)
    #Inspringmovie = happy(user_items, request.user.id)
    #ThrillingmovieInfo = thrilling(user_items, request.user.id)
    return render(request, 'movieHome.html', {'page':'movies', 'allmovies': all_movies, 'pastwatched': pastwatch, 'angermovieInfo':angermovies, 'AnticipationmovieInfo':'Anticipationmovie', 'confusingmovieInfo':"confusingmovies", 'DepressingmovieInfo':'Depressingmovie','SadmovieInfo':'Sadmovie','ExcitedmovieInfo':'Excitedmovie','HappymovieInfo':'Happymovie','InspringmovieInfo':'Inspringmovie','ThrillingmovieInfo':'Thrillingmovie'})

def getsimilarmovies(id):
    similar = "https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=bc262bfb921192a51c8cf66453a8db3c&language=en-US&page=1"
    similarlink = similar.format(movie_id = int(id))
    
    with urllib.request.urlopen(similarlink) as url:
        data = json.loads(url.read().decode())
        print(json.dumps(data, indent=1))
        return data 

def movie(request, id):
    try:
        linkobj = links.objects.get(tmdbid=int(id))
        Ratings.objects.get_or_create(movieid=linkobj.movieid, user=request.user)
    except links.DoesNotExist:
        pass
    apilink = "http://api.themoviedb.org/3/movie/{tmdbmovieid}?api_key=bc262bfb921192a51c8cf66453a8db3c&append_to_response=videos"
    link = apilink.format(tmdbmovieid = int(id))
    moviedetail = dict()

    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode())
        moviedetail = data
        print(type(data))
    similarmovies = getsimilarmovies(id)
    return render(request, 'movieINFO.html', {'page':'movies','moviedetail': moviedetail, 'similarmovies': similarmovies})
    
def searchmovie(request):
    apilink = 'https://api.themoviedb.org/3/search/movie?api_key=bc262bfb921192a51c8cf66453a8db3c&language=en-US&query={query}&page={page}&include_adult=false'
    query = request.GET.get('query')
    query = query.replace(" ", "%20")
    page = request.GET.get('page')
    link = apilink.format(query = query, page = page)
    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode())
        print(type(data))
        return render(request, 'movieSEARCH.html', {'page':'movies', 'movies': data})