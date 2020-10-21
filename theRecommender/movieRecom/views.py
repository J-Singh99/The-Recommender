from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
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

context = {
        'movieInfo': movieInfo
    }

def test(request):
	return render(request, 'movieBASE.html', context = context)


'''
def register_event(request,id):
    if (request.user.is_authenticated):
        obj=RegisteredEvents()
        #evt=events.objects.get(id=id)
        obj.event=events.objects.get(pk=id)
        obj.user=request.user
        obj.save()
        messages.success(request, "Registered for event Successfully!!")
    return redirect('events')

def read_more(request,id):
    if (request.user.is_authenticated):
        evt = events.objects.get(pk=id)
    return render(request, 'readmore.html',{'evt':evt})

def event_feed(request):
    if (request.user.is_authenticated):
        #for now lets just render all events
        evt = events.objects.all()
        return render(request, 'event.html', {'page':'events','evt':evt})
'''