from django import forms
from .models import *

class RegisterFolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['title']

        # error_messages = {
        #     "nome":{
        #         "required": "O nome é obrigatório para realizar o registro!",
        #         "invalid": "Por favor, insira um nome válido!",
        #     },
        # }

        # widgets = {
        #     "nome": forms.TextInput(attrs={'placeholder':'Insira o nome...'}),
        # }

        # labels = {
        #     "nome": 'Nome: ',
        # }