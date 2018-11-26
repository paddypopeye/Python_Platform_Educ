# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.urlresolvers import reverse
from common.decorators import ajax_required
#import time 
from .models import Chatpop
#from FB import FB
#from Parse import Parse
#from twitterSearch import twitterSearch

def Logout(request):
    #logout(request)
    Chatpop.objects.all().delete()
    logout(request)
    return redirect('/')

def Home(request):
    users1 = User.objects.all()
    sessions = Session.objects.all()
    users = []
    for user in User.objects.all():
        if user.is_authenticated():
            users.append(user)
    c = Chatpop.objects.all()
    userto = []
    for user_to in c:
        if user.is_authenticated():
            userto.append(user_to.user_to)

    return render(request, "chatpop/chatpop1.html", {'home': 'active', 'chat': c, 'users': users, 'sessions':sessions,'userto':userto})

@csrf_exempt
def Post(request):
        if request.method == 'POST':
            msg = request.POST.get('chat-msg', 'testingNEW')
            userto = request.POST.get('userto')
            user_to = User.objects.get(username=userto)
            usertoid = user_to.id

            c = Chatpop(user=request.user, message=msg, user_to=user_to)
            print "This is the userto ", userto
            print "This is the usertoid ", usertoid
        #if(msg[0:6] == "Robot:"):
            #callRobot(msg, request)
            msg = c.user.username+" : " + msg
            c = Chatpop(user=request.user, message=msg, user_to=user_to)
            print "this is the userto.id type", type(user_to.id)
            if msg != '':
                c.save()
        #img = src="https://scontent-ord1-1.xx.fbcdn.net/hprofile-xaf1/v/t1.0-1/p160x160/11070096_10204126647988048_6580328996672664529_n.jpg?oh=f9b916e359cd7de9871d8d8e0a269e3d&oe=576F6F12"
        return JsonResponse({ 'msg': msg, 'user': c.user.username, 'userto': userto, 'usertoid':usertoid })
    

def Messages(request):
    c = Chatpop.objects.all()
    return render(request, 'chatpop/messages.html', {'chat': c})

def get_absolute_url(request):
    return reverse('chatpop:home', args=[request.user_to])


'''
def chatpop(request):
	return render(request, 'chatpop/chatpop1.html')
'''