from django.shortcuts import render
from . import forms
from ProApp.models import User
# Create your views here.

def index(request):
    return render(request,'ProApp/index.html')

def user(request):
    user_list  = User.objects.order_by('first_name')
    dict = {'user_data': user_list}
    return render(request,'ProApp/user.html',context=dict)

def disp_form(request):
    form = forms.SignUp()

    if request.method == 'POST':
        form = forms.SignUp(request.POST)

        if form.is_valid():
            form.save()
            return index(request)

    return render(request,'ProApp/sign_up.html',{'form_data':form})
