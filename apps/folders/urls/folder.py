from django.urls import path, include
from folders.views import *

urlpatterns = [
    # FOLDER
    path('folder/', include([
        path('register/', register_folder, name="register_folder"),

        path('<slug:slug_folder>/', include([
            path('register/', register_sub_folder, name="register_sub_folder"),
            path('list/', list_sub_folders, name="list_sub_folders"),      
            path("change/", change_folder, name="change_folder"),
            path("delete/", delete_folder, name="delete_folder"),  
        ])),
    ])),
]

