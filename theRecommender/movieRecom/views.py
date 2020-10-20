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


def test(request):
	return render(request, 'movieBASE.html')


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