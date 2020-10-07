from django.shortcuts import render
from django.shortcuts import redirect
from .models import Message, Group, JoinedGroups, JoinedUser
from django.urls import reverse
from .forms import CreateGroup
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q
# Create your views here.

def userorgrouplist(user:User):
    userlist = JoinedUser.objects.all().filter(Q(sender=user) | Q(receiver=user))
    print(userlist)
    grouplist = JoinedGroups.objects.all().filter(user=user)
    print(grouplist)
    return userlist, grouplist

@login_required
def chat(request):
    userlist, grouplist = userorgrouplist(request.user)
    for i in userlist:
        print(i.receiver)
    return render(request, 'chat.html' , {'page':'chat', 'userlist':userlist, 'grouplist':grouplist} )

@login_required
def chat_personal(request, pk):
    if(int(pk) == int(request.user.pk)):
        return redirect('chat')
    if( int(pk) > int(request.user.pk)):
        JoinedUser.objects.get_or_create(sender=request.user, receiver=User.objects.get(pk=pk))
    else:
        JoinedUser.objects.get_or_create(receiver=request.user, sender=User.objects.get(pk=pk))
    uniquekey = uniquepk(str(pk), str(request.user.pk))
    group = 'chat_personal_%s' % uniquekey
    chat_messages = Message.objects.all().filter(group=group).order_by('timestamp')
    userlist, grouplist = userorgrouplist(request.user)
    return render(request, 'chat_personal.html' , {'page':'chat', 'pk': pk,'chat_messages': chat_messages, 'userlist':userlist, 'grouplist':grouplist} )

@login_required
def chat_grp(request, pk):
    JoinedGroups.objects.get_or_create(group=Group.objects.get(pk=pk), user=request.user)
    group = 'chat_grp_%s' % str(pk) 
    chat_messages = Message.objects.all().filter(group=group).order_by('timestamp')
    userlist, grouplist = userorgrouplist(request.user)
    
    return render(request, 'chat_grp.html' , {'page':'chat', 'pk': pk, 'chat_messages': chat_messages, 'userlist':userlist, 'grouplist':grouplist} )

@login_required
def search(request):
    if request.is_ajax and request.method == "POST":
        searchText = request.POST.get("searchText", "")
        userlist = User.objects.all().filter(username=searchText)
        print(userlist)
        user= serializers.serialize('json', list(userlist), fields=('username', 'is_active'))
        group_list = Group.objects.all().filter(group_name__contains=searchText)[:10]
        grps = serializers.serialize('json', list(group_list), fields=('group_name', 'description', "image"))
        return JsonResponse({"instance": grps, "user":user}, status=200)
    return JsonResponse({"error": ""}, status=400)

@login_required
def create_group(request):
    if request.method == 'POST' :
        form = CreateGroup(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            pk = form.save(user).pk
            #messages.success(request, "Assignment Uploaded Successfully!!")
            return redirect(reverse('grp_chat', kwargs={'pk':pk}))
        else:
            return render(request, 'create_grp.html', {'form':form})
    form = CreateGroup()
    return render(request, 'create_grp.html', {'form':form})

def uniquepk(pk1, pk2):
    if(pk1 > pk2):
        return pk1 + '_to_' + pk2
    else:
        return pk2 + '_to_' + pk1