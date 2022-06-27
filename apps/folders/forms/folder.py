from django import forms
from folders.models import *

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['title']

        error_messages = {
            'title':{
                "required": "O nome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um nome válido!",
            },
        }