from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from . import models

## Create your views here.


class SchoolListView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'

# class CBView(View):
#     def get(self,request):
#         return HttpResponse("HELLO CBV")

# class IndexView(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['inject_me'] = 'BASIC STUFF'
#         return context
