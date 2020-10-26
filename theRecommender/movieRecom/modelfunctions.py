from .mlModels.mlModel import  All, Anger, Confusing, Anticipation, Depressing, Sad, Excited, Happy, Inspring, Thrilling
from .mlModels.MovieLens import MovieLens
from .models import links, Ratings
import urllib.request, json 

def extractmovies(algo, ml, user_items, userid, start=0, end=10):
    print("Computing recommendations...")
    testSet = algo.dataset.GetAntiTestSetForUserData(userid, user_items)
    print(userid)
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
        link = apilink.format(tmdbmovieid=linkobj.tmdbid)
        try:
            with urllib.request.urlopen(link) as url:
                data = json.loads(url.read().decode())
                movies.append(data)
        except: 
            print("error")
    return movies

def getmovies(moviesidlist):
    movies = list()
    apilink = "http://api.themoviedb.org/3/movie/{tmdbmovieid}?api_key=bc262bfb921192a51c8cf66453a8db3c&append_to_response=videos"
    for i in moviesidlist:
        if len(movies)>10:
            break
        try:
            linkobj = links.objects.get(movieid=int(i))
            link = apilink.format(tmdbmovieid=linkobj.tmdbid)
            with urllib.request.urlopen(link) as url:
                data = json.loads(url.read().decode())
                movies.append(data)
        except: 
            print("error")
    return movies


def anger(user_items, userid):
    algo = Anger.algo
    ml = MovieLens(Anger.contains)
    ml.loadMovieLensLatestSmall()
    return extractmovies(algo, ml, user_items, userid)

def anticipation(user_items, userid):
    algo = Anticipation.algo
    ml = MovieLens(Anticipation.contains)
    ml.loadMovieLensLatestSmall()
    return extractmovies(algo, ml, user_items, userid)

def confusing(user_items, userid):
    algo = Confusing.algo
    ml = MovieLens(Confusing.contains)
    ml.loadMovieLensLatestSmall()
    return extractmovies(algo, ml, user_items, userid)

def depressing(user_items, userid):
    algo = Depressing.algo
    ml = MovieLens(Depressing.contains)
    ml.loadMovieLensLatestSmall()
    return extractmovies(algo, ml, user_items, userid)

def sad(user_items, userid):
    algo = Sad.algo
    ml = MovieLens(Sad.contains)
    ml.loadMovieLensLatestSmall()
    return extractmovies(algo, ml, user_items, userid)

def excited(user_items, userid):
    algo = Excited.algo
    ml = MovieLens(Excited.contains)
    ml.loadMovieLensLatestSmall()
    return extractmovies(algo, ml, user_items, userid)

def happy(user_items, userid):
    algo = Happy.algo
    ml = MovieLens(Happy.contains)
    ml.loadMovieLensLatestSmall()
    return extractmovies(algo, ml, user_items, userid)

def inspring(user_items, userid):
    algo = Inspring.algo
    ml = MovieLens(Inspring.contains)
    ml.loadMovieLensLatestSmall()
    return extractmovies(algo, ml, user_items, userid)

def thrilling(user_items, userid):
    algo = Thrilling.algo
    ml = MovieLens(Thrilling.contains)
    ml.loadMovieLensLatestSmall()
    return extractmovies(algo, ml, user_items, userid)

def allmovies(user_items, userid):
    algo = All.algo
    ml = MovieLens(All.contains)
    ml.loadMovieLensLatestSmall()
    return extractmovies(algo, ml, user_items, userid)

