# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from actions.models import Action
from friendship.models import Friend, FriendshipRequest, Follow
from actions.utils import  create_action

# Create your views here.
@login_required
def request_friends(request, pk):
	other_user = User.objects.get(pk=pk)
	new_relationship = Friend.objects.add_friend(request.user,other_user)
	return redirect(reverse('account:dashboard'))

@login_required
def acceptRequest(request, pk):
	unreads = FriendshipRequest.objects.select_related().all()
	print (unreads)
	req = unreads.get(pk=pk)
	req.accept()
	return redirect(reverse('account:dashboard'))

@login_required
def rejectRequest(request, pk):
	unreads = FriendshipRequest.objects.select_related().all()
	print (unreads)
	req = unreads.get(pk=pk)
	print req
	req.reject()
	req.delete()
	return redirect(reverse('account:dashboard'))

@login_required
def removeFriend(request, pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	owner = request.user
	Friend.objects.remove_friend(owner, user)
	return redirect(reverse('account:dashboard'))

@ajax_required
@require_POST
@login_required
def user_follow(request):
	user_id = request.POST.get('id')
	action = request.POST.get('action')
	if user_id and action:
		try:
			user = User.objects.get(id=user_id)
			if action == 'follow':
				Contact.objects.get_or_create(user_from=request.user, user_to=user)
				create_action(request.user, 'is following', user)
			else:
				Contact.objects.filter(user_from=request.user, user_to=user).delete()
				create_action(request.user, 'is no longer following', user)

			return JsonResponse({'status': 'ok'})
		except User.DoesNotExist:
			return JsonResponse({'status': 'ko'})
	return JsonResponse({'status': 'ko'})

@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'account/user/list.html', {'section': 'people',
                                                      'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section': 'people',
                                                        'user': user})


@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Profile successfully updated')
		else:
			messages.error(request, 'Error editing your profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
	return render(request, 'account/edit.html', {'user_form' :user_form,
													'profile_form': profile_form })
@login_required
def dashboard(request):
	users = User.objects.all()
	user = User.objects.get(pk=request.user.id)
	all_friends = Friend.objects.friends(request.user)
	requests = Friend.objects.unread_requests(request.user)
	unreads = FriendshipRequest.objects.select_related().all()
	rejects = Friend.objects.rejected_requests(user=request.user)
	
	
	print "all_friends",(all_friends)
	print "unreads",(unreads)
	print "rejects",(rejects)
	actions = Action.objects.exclude(user=request.user)
	following_ids = request.user.following.values_list('id',flat=True)
	if following_ids:
		# If user is following others, retrieve only their actions
		actions = actions.filter(user_id__in=following_ids).select_related('user', 'user__profile').prefetch_related('target')
	actions = actions[:6]
	return render(request,'account/dashboard.html',
		{'section': 'dashboard','actions': actions, 
		'users': users, 'all_friends':all_friends,
		'rejects':rejects, 'requests':requests, 
		'unreads': unreads })

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)	
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username = cd['username'], password = cd['password'])
			 
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated successfully')
				else:
					return HttpResponse('Disabled account')
			else	:
				return H0ttpResponse('Invalid login')
	else:
		form = LoginForm()

	return render(request, 'account/login.html', {'form':form })


def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			profile = Profile.objects.get(user=new_user)
			create_action(new_user, 'has created an account', profile)
			return render(request, 'account/register_done.html', {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'account/register.html', {'user_form': user_form})