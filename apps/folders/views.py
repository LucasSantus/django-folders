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

def register_sub_folder(request, slug):
    folder = Folder.objects.get(slug = slug)
    form = RegisterFolderForm()
    if request.method == "POST":
        form = RegisterFolderForm(request.POST)
        if form.is_valid():
            # form.save(commit = False)
            form.sub_folder = True
            form.folder = folder
            form.save()

            messages.success(request, f"Registered sucess!")
            return redirect('/')

    context = {
        'form': form,
        'action': 'Register'
    }

    return render(request, "folders/register_folder.html", context)

def list_sub_folders(request, slug_folder):
    folder = Folder.objects.get(slug = slug_folder)
    sub_folders = Folder.objects.filter(folder = folder)
    
    context = {
        'folder': folder,
        'sub_folders': sub_folders
    }

    return render(request, "folders/list_sub_folders.html", context)