from django.urls import path
from home.views import index

urlpatterns = [
    # INDEX
    path("", index, name="index"),
]
