from django.shortcuts import render
from folders.models import Folder

def index(request):
    folders = Folder.objects.filter(sub_folder = False)
    context = {
        'folders': folders,
    }

    return render(request, "home/index.html", context)