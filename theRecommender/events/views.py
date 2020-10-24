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
from .models import Post,events,club,RegisteredEvents,AdminOf
from .forms import uploadeventform,uploadclubform


#from .models import Post
def add_club(request):
    if (request.user.is_authenticated):
        if request.method == 'POST':
            form = uploadclubform(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "CLUB Uploaded Successfully!!")
        else:
            form = uploadclubform()
            return render(request, 'addclub.html', {'page':'events','form':form})
    else:
        messages.error(request, "Authetication required first!")
        
    return redirect('events')

def delete_event(request,id):
    evt = events.objects.get(pk=id)
    if (request.user.is_authenticated and request.user==evt.creator ):
        events.objects.get(pk=id).delete()
        messages.success(request, "Deleted Event Successfully!!")
    else:
        messages.success(request, "YOU ARE NOT AUTHORISED TO DELETE THIS EVENT BECAUSE YOU ARE NOT ADMIN!!")
    return redirect('events')

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

def add_event(request):
    if (request.user.is_authenticated):
        if request.method == 'POST':
            form = uploadeventform(request.POST)
            if form.is_valid():
                clubtag = form.cleaned_data['tag']
                form.save(request.user,clubtag)
                messages.success(request, "Event Uploaded Successfully!!")
        else:
            form = uploadeventform()
            return render(request, 'upload_event.html', {'page':'events','form':form})
    else:
        messages.error(request, "Authetication required first!")
    return redirect('events')


def test(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'templates/test.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})