from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import Tasks
from .forms import CreateTask
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def get_pages(user_pk):
    my_model = Tasks.objects.all().filter(user=user_pk,completed=False).order_by('deadline')
    number_of_item = 2
    paginatorr = Paginator(my_model, number_of_item)
    page_range = paginatorr.num_pages
    return page_range

def index_2(request):
    form = CreateTask()
    print("index")
    tasks = Tasks.objects.all().filter(user=request.user.pk).order_by('deadline')
    return render(request, 'index.html', {'page': 'index', 'tasks': tasks, 'form': form})

#if request.method == 'POST':
 #       form = CreateTask(request.POST)
  #      print(request.POST.get('task'))
   #     if form.is_valid():
    #        form.save(request.user)

def index(request):
    form = CreateTask()
    #model
    tasks=Tasks.objects.all().filter(user=request.user.pk).order_by('deadline')
    my_model = Tasks.objects.all().filter(user=request.user.pk,completed=False).order_by('deadline')
    number_of_item = 2
    paginatorr = Paginator(my_model, number_of_item)
    first_page = paginatorr.page(1).object_list
    page_range = paginatorr.page_range
    result = paginatorr.page(1)
    if request.method == 'POST':
        page_n = request.POST.get('page_n', None) #getting page number
        results = list(paginatorr.page(page_n).object_list.values('id', 'task', 'deadline', 'completed'))
        return JsonResponse({"results":results})
    return render(request, 'index.html', {'page': 'index', 'tasks': tasks, 'form': form,'results':result,'first_page':first_page,'page_range':page_range})

@login_required
def addTask(request):
    if request.is_ajax and request.method == "POST":
        form = CreateTask(request.POST)
        print("addtask called")
        if form.is_valid():
            task = form.save(request.user)
            latest_id=task.id
            task_list=[]
            task_list.append(task)
            latest_task = serializers.serialize('json', task_list, fields=('task', 'deadline'))
            page_range=get_pages(request.user.pk)
            return JsonResponse({"task": latest_task,"id":latest_id,"page_range":page_range}, status=200)
    return JsonResponse({"error": ""}, status=400)


def deleteTask(request, id):
    print("delete called")
    print(request)
    if request.is_ajax:
        print("deleteajax called")
        task = Tasks.objects.filter(id=id).delete()
        page_range=get_pages(request.user.pk)
        return JsonResponse({"page_range":page_range}, status=200)
    return JsonResponse({"error": ""}, status=400)

def markcomplete(request):
    if request.is_ajax:
        id_list=request.GET.getlist('id[]')
        print(id)
        for i in id_list:
           t = Tasks.objects.get(id=i)
           t.completed = True
           t.save(update_fields=['completed']) 
           page_range=get_pages(request.user.pk)
        return JsonResponse({"page_range":page_range}, status=200)
    return JsonResponse({"error": ""}, status=400)





