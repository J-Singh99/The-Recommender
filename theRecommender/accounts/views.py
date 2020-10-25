from django.shortcuts import render,redirect
from .models import User, Tasks
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
import json
from django.contrib import messages
from .forms import LoginForm, CustomUserCreationForm, CreateTask
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.http import HttpResponse
# Create your views here.


def CustomSignUpView(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():  
            image = request.FILES['image']
            user = form.save(image)
            login(request, user)
            messages.success(request, "You are logged in successfully!!! ")
            return redirect('/')
        else:
            return render(request, 'account.html', {'page':'index', 'include': 'signup.html', 'form': form})
    else:
        form = CustomUserCreationForm()
        print(form)
        return render(request, 'account.html', {'page':'index', 'include': 'signup.html', 'form': form})

def CustomLoginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                messages.success(request, "You are logged in successfully!!! ")
                return redirect('/')
            else:
                return render(request, 'account.html', {'page':'index', 'include': 'signin.html', 'form': form})
        else:
            return render(request, 'account.html', {'page':'index', 'include': 'signin.html', 'form': form})
    form = LoginForm()
    return render(request, 'account.html', {'page':'index', 'include': 'signin.html', 'form':form })


def signout(request):
    logout(request)
    messages.info(request, "You are logged out successfully!!! ")
    return redirect('/')


global number_of_item
number_of_item=2

def get_pages(user_pk):
    my_model   = Tasks.objects.all().filter(user=user_pk,completed=False).order_by('deadline')
    paginatorr = Paginator(my_model, number_of_item)
    page_range = paginatorr.num_pages
    return page_range

def get_comp_pages(user_pk):
    my_model     = Tasks.objects.all().filter(user=user_pk,completed=True)
    paginatorr   = Paginator(my_model, number_of_item)
    page_range_2 = paginatorr.num_pages
    return page_range_2

def todo(request):
    form = CreateTask()
    comp_tasks = Tasks.objects.all().filter(user=request.user.pk,completed=True)
    my_model   = Tasks.objects.all().filter(user=request.user.pk,completed=False).order_by('deadline')
    paginatorr   = Paginator(my_model, number_of_item)
    paginatorr_2 = Paginator(comp_tasks, number_of_item)
    first_page   = paginatorr.page(1).object_list
    first_page_2 = paginatorr_2.page(1).object_list
    page_range   = paginatorr.page_range
    page_range_2 = paginatorr_2.page_range
    result       = paginatorr.page(1)
    result_2     = paginatorr_2.page(1)
    
    if request.method == 'POST':
        page_n    = request.POST.get('page_n', 1)
        page_n_2  = request.POST.get('page_n_2', 1)
        results   = list(paginatorr.page(page_n).object_list.values('id', 'task', 'deadline'))
        results_2 = list(paginatorr_2.page(page_n_2).object_list.values('id', 'task'))
        return JsonResponse({"results":results,"results_2":results_2})
    return render(request, 'todowithindex.html', {'page': 'todolist', 'first_page_2': first_page_2, 'form': form,'results':result,'results_2':result_2,'first_page':first_page,'page_range':page_range,'page_range_2':page_range_2})


def index(request):
    form = CreateTask()
    comp_tasks = Tasks.objects.all().filter(user=request.user.pk,completed=True)
    my_model   = Tasks.objects.all().filter(user=request.user.pk,completed=False).order_by('deadline')
    paginatorr   = Paginator(my_model, number_of_item)
    paginatorr_2 = Paginator(comp_tasks, number_of_item)
    first_page   = paginatorr.page(1).object_list
    first_page_2 = paginatorr_2.page(1).object_list
    page_range   = paginatorr.page_range
    page_range_2 = paginatorr_2.page_range
    result       = paginatorr.page(1)
    result_2     = paginatorr_2.page(1)
    
    if request.method == 'POST':
        page_n    = request.POST.get('page_n', 1)
        page_n_2  = request.POST.get('page_n_2', 1)
        results   = list(paginatorr.page(page_n).object_list.values('id', 'task', 'deadline'))
        results_2 = list(paginatorr_2.page(page_n_2).object_list.values('id', 'task'))
        return JsonResponse({"results":results,"results_2":results_2})
    return render(request, 'todowithindex.html', {'page': 'index', 'include': 'index.html', 'first_page_2': first_page_2, 'form': form,'results':result,'results_2':result_2,'first_page':first_page,'page_range':page_range,'page_range_2':page_range_2})

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
            page_range  = get_pages(request.user.pk)
            page_range_2= get_comp_pages(request.user.pk)
            return JsonResponse({"task": latest_task,"id":latest_id,"page_range":page_range,"page_range_2":page_range_2}, status=200)
    return JsonResponse({"error": ""}, status=400)

@login_required
def editTask(request):
    if request.method == "POST":
        print("save")
        new_id      = request.POST.get("edit_id_view")
        new_task    = request.POST.get("edited_task")
        new_deadline= request.POST.get("edited_time")
        t = Tasks.objects.get(id=new_id)
        t.task=new_task
        t.deadline=new_deadline
        t.save(update_fields=['task','deadline'])
        return redirect('/')
    return redirect('/') 


@login_required
def deleteTask(request, id):
    print("delete called")
    print(request)
    if request.is_ajax:
        print("deleteajax called")
        task        = Tasks.objects.filter(id=id).delete()
        page_range  = get_pages(request.user.pk)
        page_range_2= get_comp_pages(request.user.pk)
        return JsonResponse({"page_range":page_range,"page_range_2":page_range_2}, status=200)
    return JsonResponse({"error": ""}, status=400)

@login_required
def markcomplete(request):
    if request.is_ajax:
        id_list=request.GET.getlist('id[]')
        print(id)
        for i in id_list:
           t = Tasks.objects.get(id=i)
           t.completed = True
           t.save(update_fields=['completed']) 
           page_range   = get_pages(request.user.pk)
           page_range_2 = get_comp_pages(request.user.pk)
        return JsonResponse({"page_range":page_range,"page_range_2":page_range_2}, status=200)
    return JsonResponse({"error": ""}, status=400)





