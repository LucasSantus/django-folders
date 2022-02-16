from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

from folders.models import Folder

def index(request):
    folders = Folder.objects.filter()
    context = {
        'folders': folders,
    }

    return render(request, "home/index.html", context)