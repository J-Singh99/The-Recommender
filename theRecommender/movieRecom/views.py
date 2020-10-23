from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages


movieInfo = [
    {'name':'Movie1', 'rel_date':'Today', 'rating':6, 'length':'120 mins', 'Director':'Tarantino', 'random':1},
    {'name':'Movie2', 'rel_date':'Yesterday', 'rating':4, 'length':'120 mins', 'Director':'Tarantino1', 'random':2},
    {'name':'Movie3', 'rel_date':'Tomorrow', 'rating':1, 'length':'120 mins', 'Director':'Tarantino2', 'random':3},
    {'name':'Movie4', 'rel_date':'Today', 'rating':10, 'length':'120 mins', 'Director':'Tarantino3', 'random':4},
    {'name':'Movie5', 'rel_date':'Yesterday', 'rating':3, 'length':'120 mins', 'Director':'Tarantino4', 'random':5},
    {'name':'Movie6', 'rel_date':'Tomorrow', 'rating':7, 'length':'120 mins', 'Director':'Tarantino5', 'random':6},
    {'name':'Movie7', 'rel_date':'Today', 'rating':3, 'length':'120 mins', 'Director':'Tarantino6', 'random':7},
    {'name':'Movie8', 'rel_date':'Yesterday', 'rating':6, 'length':'120 mins', 'Director':'Tarantino7', 'random':8},
    {'name':'Movie9', 'rel_date':'Tomorrow', 'rating':9, 'length':'120 mins', 'Director':'Tarantino8', 'random':9},
    {'name':'Movie10', 'rel_date':'Today', 'rating':7, 'length':'120 mins', 'Director':'Tarantino9', 'random':10},
    {'name':'Movie11', 'rel_date':'Yesterday', 'rating':2, 'length':'120 mins', 'Director':'Tarantino10', 'random':11},
    {'name':'Movie12', 'rel_date':'Tomorrow', 'rating':3, 'length':'120 mins', 'Director':'Tarantino11', 'random':12},
    {'name':'Movie13', 'rel_date':'Today', 'rating':8, 'length':'120 mins', 'Director':'Tarantino12', 'random':13}
]

movieCard = {
    "name":"Little Miss Sunshine",
    "director":"Valerie Faris",
    "imdb":"7.8",
    "description":"A family decide to travel across the country when their daughter wants to participate in a beauty pageant, unaware of what the journey has in store for them.",
    "rel_date":"26 July 2006",
    "genre":"Adventure, Family, Relationships",
    "run_time":"122 mins",
    "cast":"Steve, Paul, Greg, Alan",
    "trailer":"https://www.youtube.com/watch?v=wvwVkllXT80",
    'movieInfo': movieInfo
    }

context = {
        'movieInfo': movieInfo
    }




def test(request):
    return render(request, 'movieBASE.html', context = context)



def main(request):
    return render(request, 'movieHome.html', context = context)

def movie(request):
	return render(request, 'movieINFO.html', context = movieCard)

def search(request):
    return render(request, 'movieSEARCH.html', context = movieCard)