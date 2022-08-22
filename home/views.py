from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoCreateForms, TodoUpdateForm
from django.contrib import messages


def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {'todos': all})

def detail(request, todo_id):
    todoid = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo_id': todoid})

def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request,'todo deleted seccessfully', 'success')
    return redirect('home')

def create(request):
    if request.method == 'POST':
        form = TodoCreateForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['titel'], body=cd['body'],created=cd['created'])
            messages.success(request, 'todo create successfully', 'success')
            return redirect('home')
    else:
        form = TodoCreateForms()
    return render(request, 'create.html', {'form': form})

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'todo updated successfully', 'success')
            return redirect('detail', todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form':form})

