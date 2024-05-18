from django.shortcuts import render, redirect, get_object_or_404
from .models import UserData
from .forms import UserForms
from django.contrib.auth import authenticate, login


# Create your views here.
from django.contrib.auth.decorators import login_required

def user_list(request):
    users = UserData.objects.all()
    context = {'users': users}  
    return render(request, 'index.html' ,context)

# def create_user_form(request):
#     return render(request, 'add.html');

def user_create(request):
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForms()
        return render(request, 'add.html', {'form': form})

def user_update(request, id):
    user = get_object_or_404(UserData, id=id)
    if request.method == 'POST':
        form = UserForms(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForms(instance=user)
    return render(request, 'update.html', {'form': form})

def user_delete(request, id):
    user = get_object_or_404(UserData, id=id)
    user.delete()
    return redirect('user_list')
