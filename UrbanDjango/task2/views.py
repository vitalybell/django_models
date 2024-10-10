from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def show_task_2(requests):
    return render(requests,  'func_template.html')

class show_task_class_2(TemplateView):
    template_name = 'class_template.html'
