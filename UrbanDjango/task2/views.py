from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def info_func(request):
    return render(request, 'func_template.html')

class InfoClass(TemplateView):
    template_name = 'class_template.html'