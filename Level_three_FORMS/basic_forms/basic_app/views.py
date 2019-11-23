from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

def form_view(request):
    form = forms.First_form()

    if request.method == 'POST':
        form = forms.First_form(request.POST)

        if form.is_valid():
            # TO DO CODE
            print("Validated!!!")
            print("Name : " + form.cleaned_data['name'])
            print("Email : " + form.cleaned_data['email'])
            print("Text : " + form.cleaned_data['text'])

    return render(request,'basic_app/form_page.html',{'form_here':form})
