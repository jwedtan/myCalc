from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render , redirect
from .forms import HomeForm
from Calc.models import Calculations


# Create your views here.
class HomePage(TemplateView):
    template_name = 'Calc/home.html'

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
            #return redirect ('home:home')

        args = {'form': form , 'result': answer}
        self.history(request)
        return render(request, self.template_name, args )
    
    def history(self,request):
        form = HomeForm()
        data = Calculations.objects.all()
        print data
        # args2 = {'form': form , 'history': data}
        return render(request, self.template_name, {'calculation': data})


        