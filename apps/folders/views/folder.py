from django.shortcuts import render, redirect
from folders.forms import *
from django.contrib import messages
from django.shortcuts import get_object_or_404, get_list_or_404
from home.default_messages import *

def register_folder(request):
    form = FolderForm()
    if request.method == "POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, DEFAULT_MESSAGES["FOLDER_ADD"])
            return redirect('/')
    context = {
        'form': form,
        'action': 'Registrar'
    }
    return render(request, "folders/register_folder.html", context)

def register_sub_folder(request, slug_folder):
    folder = get_object_or_404(Folder.objects.select_related("folder"), slug = slug_folder)
    breadcrumbs = folder.breadcrumbs(folder)

    form = FolderForm()
    if request.method == "POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            sub_folder = form.save(commit = False)
            sub_folder.sub_folder = True
            sub_folder.folder = folder
            sub_folder.save()
            messages.success(request, DEFAULT_MESSAGES["FOLDER_ADD"])
            return redirect('list_sub_folders', folder.slug)
    context = {
        'form': form,
        'breadcrumbs': breadcrumbs,
        'action': 'Registrar'
    }
    return render(request, "folders/register_folder.html", context)

def list_sub_folders(request, slug_folder):
    folder = get_object_or_404(Folder.objects.select_related("folder"), slug = slug_folder)
    folders = Folder.objects.select_related("folder").filter(folder = folder)

    # breadcrumbs = []

    # aux = folder
    # breadcrumbs.append(folder)

    # while aux.sub_folder != False:
    #     if len(breadcrumbs) < 5:
    #         aux = aux.folder
    #         breadcrumbs.append(aux)
    #     else:
    #         break

    breadcrumbs = folder.breadcrumbs(folder)

    context = {
        'folder': folder,
        'folders': folders,
        'breadcrumbs': breadcrumbs
    }
    return render(request, "home/index.html", context)

def change_folder(request, slug_folder):
    folder = get_object_or_404(Folder.objects.select_related("folder"), slug = slug_folder)
    
    form = FolderForm(instance = folder)
    if request.method == "POST":
        form = FolderForm(request.POST, instance = folder)
        if form.is_valid():
            form.save()
            messages.success(request, DEFAULT_MESSAGES["FOLDER_CHANGED"])
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
    folder = get_object_or_404(Folder.objects.select_related("folder"), slug = slug_folder)

    slug_folder_father = None
    if folder.folder:
        slug_folder_father = folder.folder.slug

    folder.delete()

    messages.success(request, DEFAULT_MESSAGES["FOLDER_DELETE"])

    if slug_folder_father:
        return redirect('list_sub_folders', slug_folder_father)
    else:
        return redirect('/')