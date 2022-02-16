from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

def register_folder(request):
    form = RegisterFolderForm()
    if request.method == "POST":
        form = RegisterFolderForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, f"Registered sucess!")

            return redirect('/')

    context = {
        'form': form,
        'action': 'Register'
    }

    return render(request, "folders/register_folder.html", context)

