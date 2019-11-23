from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')


def other(request):
    dict = {'num':100 , 'text':'Hello World'}
    return render(request,'basicapp/other.html',context=dict)


def relative(request):
    return render(request,'basicapp/relative_url_templates.html')
