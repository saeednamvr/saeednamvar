from django.shortcuts import render,redirect
from  django.http import HttpResponse
from  .models import Todo
from django.contrib import messages
from .forms import TodoCreatForm, TodoUpdateForm

# Create your views here.
def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {'all' : all})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo':todo})

def delete(requset, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(requset,'todo deleted successfully','success')
    return redirect('home')

def create(request):
    if request.method == 'POST':
        form = TodoCreatForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'],body=cd['body'],created=cd['created'])
            messages.success(request, 'Todo created successfully', 'success')
            return redirect('home')
    else:###Get
        form = TodoCreatForm()
    return render(request, 'create.html',{'form':form})

def update(requset, todo_id):
    todo =Todo.objects.get(id=todo_id)
    if requset.method == 'POST':
        form =TodoUpdateForm(requset.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(requset, 'your todo updated successfuly', 'success')
            return redirect('details',todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(requset, 'update.html', {'form':form})