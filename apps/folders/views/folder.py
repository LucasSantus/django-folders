from django.shortcuts import render, redirect
from folders.forms import *
from django.contrib import messages

def register_folder(request):
    form = FolderForm()
    if request.method == "POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Folder Registrado com sucesso!")
            return redirect('/')

    context = {
        'form': form,
        'action': 'Register'
    }
    return render(request, "folders/register_folder.html", context)

def register_sub_folder(request, slug_folder):
    folder = Folder.objects.get(slug = slug_folder)
    form = FolderForm()
    if request.method == "POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            sub_folder = form.save(commit = False)
            sub_folder.sub_folder = True
            sub_folder.folder = folder
            sub_folder.save()

            messages.success(request, f"Folder Registrado com sucesso!")
            return redirect('list_sub_folders', folder.slug)

    context = {
        'form': form,
        'action': 'Register'
    }
    return render(request, "folders/register_folder.html", context)

def list_sub_folders(request, slug_folder):
    folder = Folder.objects.select_related('folder').get(slug = slug_folder)
    folders = Folder.objects.select_related('folder').filter(folder = folder)

    breadcrumbs = []

    aux = folder
    breadcrumbs.append(folder)

    while aux.sub_folder != False:
        if len(breadcrumbs) < 5:
            aux = aux.folder
            breadcrumbs.append(aux)
        else:
            break

    context = {
        'folder': folder,
        'folders': folders,
        'breadcrumbs': breadcrumbs
    }
    return render(request, "home/index.html", context)

def change_folder(request, slug_folder):
    folder = Folder.objects.select_related('folder').get(slug = slug_folder)
    
    form = FolderForm(instance = folder)
    if request.method == "POST":
        form = FolderForm(request.POST, instance = folder)
        if form.is_valid():
            form.save()
            messages.success(request, "Folder alterado com sucesso!")
            if folder.sub_folder:
                return redirect('list_sub_folders', slug_folder)
            else:
                return redirect('/')
    
    context = {
        "form": form,
        "action": "Modificar" 
    }
    return render(request, "folders/register_folder.html", context)

def delete_folder(request, slug_folder):
    folder = Folder.objects.get(slug = slug_folder)
    messages.success(request, "Folder removido com sucesso!")
    if folder.sub_folder:
        folder.delete()
        return redirect('list_sub_folders', slug_folder)
    else:
        folder.delete()
        return redirect('/')