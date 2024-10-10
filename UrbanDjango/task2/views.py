from django.shortcuts import render

# Create your views here.
def show_task_2(requests):
    return render(requests,  'second_task/func_template.html')
