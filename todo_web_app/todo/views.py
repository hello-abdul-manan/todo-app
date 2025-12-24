from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

# List all todos for logged-in user
@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'todo/todo_list.html', {'todos': todos})

# Create a new todo
@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_form.html', {'form': form, 'title': 'Create Todo'})

# Update an existing todo
@login_required
def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_form.html', {'form': form, 'title': 'Update Todo'})

# Delete a todo
@login_required
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})

# Signup
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todo_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')
