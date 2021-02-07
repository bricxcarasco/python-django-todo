from django.shortcuts import render
from django.views.generic import View

from django.http import JsonResponse


from .models import Task
from .forms import TaskForm

class TaskView(View):
    def get(self, request):
        tasks = list(Task.objects.values())

        if request.is_ajax():
            return JsonResponse({'tasks': tasks}, status=200)
            
        return render(request, 'task/task.html')
