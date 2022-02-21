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
            sub_folder = form.save(commit = False)
            sub_folder.sub_folder = True
            sub_folder.folder = folder
            sub_folder.save()

            messages.success(request, f"Registered sucess!")
            return redirect('list_sub_folders', folder.slug)

    context = {
        'form': form,
        'action': 'Register'
    }

    return render(request, "folders/register_folder.html", context)

def list_sub_folders(request, slug_folder):
    folder = Folder.objects.select_related('folder').get(slug = slug_folder)
    sub_folders = Folder.objects.select_related('folder').filter(folder = folder)

    breadcrumbs = []

    aux = folder
    breadcrumbs.append(folder)

    while aux.sub_folder != False:
        print(aux.title)
        if len(breadcrumbs) < 5:
            aux = aux.folder
            breadcrumbs.append(aux)
        else:
            break

    context = {
        'folder': folder,
        'sub_folders': sub_folders,
        'breadcrumbs': breadcrumbs
    }

    return render(request, "folders/list_sub_folders.html", context)