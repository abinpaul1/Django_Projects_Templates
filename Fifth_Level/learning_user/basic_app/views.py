from django.shortcuts import render
from basic_app import forms

#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.


def index(request):
    return render(request,'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You have reached special page for logged in folks")

def reg(request):

    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(request.POST)
        profile_form = forms.UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)  #For hashing passwords
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'pro_pic' in request.FILES:
                profile.pro_pic = request.FILES['pro_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors , profile_form.errors)

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request,'basic_app/reg.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)

        user = authenticate(username = username , password = password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details")
    else:
        return render(request,'basic_app/login.html')
