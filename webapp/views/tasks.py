from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task


def add_view(request):
    if request.method == 'GET':
        return render(request, 'task_add.html')
    task_data = {
        'name': request.POST.get('name'),
        'description': request.POST.get('description'),
        'due_date': request.POST.get('due_date'),
    }
    task = Task.objects.create(**task_data)
    return redirect('task_detail', pk=task.pk)


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'to_do_list.html', context={'task': task})
