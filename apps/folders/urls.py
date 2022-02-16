from django.urls import path
from .views import *

urlpatterns = [
    # FOLDER
    path("folder/register/", register_folder, name="register_folder"),
    path("folder/register/<slug:slug>/", register_sub_folder, name="register_sub_folder"),

    path("folder/list/<slug:slug_folder>/", list_sub_folders, name="list_sub_folders"),

    # path("folder/modify/<slug:slug>/", modify_folder, name="modify_folder"),
    # path("folder/remove/<slug:slug>/", remove_folder, name="remove_folder"),
]