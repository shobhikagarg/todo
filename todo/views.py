from django.contrib import messages
# noinspection PyUnresolvedReferences
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth
# noinspection PyUnresolvedReferences
from django.http import HttpResponse
from django.shortcuts import render,redirect

# noinspection PyUnresolvedReferences
from .forms import TodoForm
# noinspection PyUnresolvedReferences
from .models import Todo


# Create your views here.
def index(request):
    tasks = Todo.objects.all()

    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = TodoForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'list.html', context)


def updateTodo(request, pk):
    task = Todo.objects.get(pk=pk)

    form = TodoForm(instance=task)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.info(request, "item is updated..")
            return redirect('/')

    context = {'form': form}

    return render(request, 'update.html', context)


def delete(request, pk):
    thing = Todo.objects.get(id=pk)

    if request.method == 'POST':
        thing.delete()
        messages.info(request, "item removed!!!")
        return redirect('/')

    context = {'thing': thing}
    return render(request, 'delete.html', context)


def profile(request):
    return render(request, 'profile.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, "welcome,Logged in successfully!")
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')
