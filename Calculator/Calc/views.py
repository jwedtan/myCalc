from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render , redirect
from .forms import HomeForm
from .models import Calculations, Result


# Create your views here.
class HomePage(TemplateView):
    template_name = 'Calc/home.html'
    model = Calculations

    def get(self, request, *args, **kwargs):
        form = HomeForm()
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = HomeForm(request.POST)
       
        if form.is_valid():
            text = form.cleaned_data['num1']
            text2 = form.cleaned_data['num2']
            cal = Calculations(text, text2)
            cal.save()
            if 'add' in request.POST:
                result = text + text2
            elif 'sub' in request.POST:
                result = text - text2
            elif 'mul' in request.POST:
                result = text * text2
            elif 'div' in request.POST:
                result = text / text2

            form = HomeForm()
            #return redirect ('home:home')

        args = {'form': form , 'result': result}
        
        return render(request, self.template_name, args )
    
    def history(self,request):
        his = Calculations.objects.all()
        return render(request, 'Calc/home.html', {'calculations': his})
