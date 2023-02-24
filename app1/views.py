from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from app1.forms import *
# Create your views here.
#model1 of template view. 
class cbvtemplate1(TemplateView):
    template_name='cbvtemplate1.html'
    

#cbv context data

class cbvcontext(TemplateView):
    template_name='cbvcontext.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='siva'
        context['age']='22'

        return context
    

 # cbv contextdata in forms.  
class cbvforms(TemplateView):
    template_name='cbvforms.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['form']=Studentform()
        return context

    def post(self,request):
        form_data=Studentform(request.POST)
        
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))