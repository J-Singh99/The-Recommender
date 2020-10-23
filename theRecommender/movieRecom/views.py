from django.shortcuts import render
from django.shortcuts import redirect
from .mlModels.MovieLens import MovieLens
from .mlModels.mlModel import Anger#, Confusing, Anticipation, , Depressing, Sad, Excited, Happy, Inspring, Thrilling
import urllib.request, json 
from .models import links


def extractmovies(algo, ml, start=0, end=10):
    print("Computing recommendations...")
    user_items = {3601, 20, 27, 3612, 30, 31, 32, 34, 35, 36, 2085, 2090, 42, 43, 48, 49, 2100, 52, 54, 55, 56, 57, 58, 59,
                  60, 61, 64, 66, 67, 68, 69, 72, 2121, 73, 75, 76, 79, 83, 86, 87, 88, 89, 90, 91, 92, 93, 2144, 97, 99,
                  100, 101, 4205, 4206, 4207, 4208, 4209, 4210, 4211, 650, 651, 142, 656, 145, 146, 659, 148, 151, 154, 156,
                  670, 674, 675, 680, 683, 684, 690, 2234, 2236, 701, 702, 709, 714, 2251, 3335, 319, 321, 322, 323, 324,
                  386, 387, 2951, 418, 423, 424, 3009, 449, 450, 452, 2520}
    testSet = algo.dataset.GetAntiTestSetForUserData(20000, user_items)
    predictions = algo.GetAlgorithm().test(testSet)

    recommendations = []

    print("\nWe recommend:")
    for userID, movieID, actualRating, estimatedRating, _ in predictions:
        intMovieID = int(movieID)
        if (intMovieID in algo.dataset.movies):
            recommendations.append((intMovieID, estimatedRating))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    movies = list()
    apilink = "http://api.themoviedb.org/3/movie/{tmdbmovieid}?api_key=bc262bfb921192a51c8cf66453a8db3c&append_to_response=videos"
    for ratings in recommendations[start:end]:
        linkobj = links.objects.get(movieid=int(ratings[0]))
        link = apilink.format(tmdbmovieid = linkobj.tmdbid)
        with urllib.request.urlopen(link) as url:
            data = json.loads(url.read().decode())
            movies.append(data)
    return movies


def anger():
    algo = Anger.algo
    ml = MovieLens(Anger.contains)
    ml.loadMovieLensLatestSmall()
    return extractmovies(algo, ml)

# def confusing():
#     algo = Confusing.algo
#     ml = MovieLens(Confusing.contains)
#     ml.loadMovieLensLatestSmall()
#     return extractmovies(algo, ml)

def movies(request):
    angermovies = anger()
    #confusingmovies = confusing()
    return render(request, 'movieHome.html', {'angermovieInfo':angermovies, 'confusingmovieInfo':'confusingmovies'})

def getsimilarmovies(id):
    similar = "https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=bc262bfb921192a51c8cf66453a8db3c&language=en-US&page=1"
    similarlink = apilink.format(tmdbmovieid = int(id))
    
    with urllib.request.urlopen(similarlink) as url:
        data = json.loads(url.read().decode())
        print(json.dumps(data, indent=1))
        return data 

def movie(request, id):
    apilink = "http://api.themoviedb.org/3/movie/{tmdbmovieid}?api_key=bc262bfb921192a51c8cf66453a8db3c&append_to_response=videos"
    link = apilink.format(tmdbmovieid = int(id))

    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode())
        print(type(data))
    similarmovies = getsimilarmovies(id)
    return render('trying.html', {'similarmovies': similarmovies})
    
def searchmovie(request):
    apilink = 'https://api.themoviedb.org/3/search/movie?api_key=bc262bfb921192a51c8cf66453a8db3c&language=en-US&query={query}&page={page}&include_adult=false'
    query = request.GET.get('query')
    page = request.GET.get('page')
    link = apilink.format(query = query, page = page)
    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode())
        print(type(data))
        redirect('movies')