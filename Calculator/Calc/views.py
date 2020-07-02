from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render , redirect
from django.utils import timezone
from .forms import HomeForm
from Calc.models import Calculations

# class HistoryView(TemplateView):
#     template_name = 'Calc/history.html'
   

# Create your views here.
class HomePage(TemplateView):
    template_name = 'Calc/home.html'
    model = Calculations
    context_object_name = "history"

    def get(self, request, *args, **kwargs):
        form = HomeForm()
       
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = HomeForm(request.POST)
        
        if form.is_valid():
            text = form.cleaned_data['num1']
            text2 = form.cleaned_data['num2']
            answer = text + text2
            
            cal = Calculations(calc1=text, calc2=text2, result=answer)
            cal.save()
            form = HomeForm()
        self.history_list(request)
        return render(request, self.template_name, {'form': form,'result': answer} )
    
    def history_list(self,request):
        context_object_name = 'history'
        # form = HomeForm()
        history = Calculations.objects.all()
        print history
        return render(request, self.template_name , {'history':history})
   



        