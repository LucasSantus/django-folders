from django.contrib import admin
from folders.models import *

# class PastaAdmin(admin.ModelAdmin):
#     list_display = ('titulo', 'vinculo', 'horario_registrado')

admin.site.register(Folder)