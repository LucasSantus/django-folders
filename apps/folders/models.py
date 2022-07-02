from django.db import models
from autoslug import AutoSlugField

class Folder(models.Model):
    title = models.CharField("title", max_length = 120)
    sub_folder = models.BooleanField(default = False, null = True, blank = True)
    folder = models.ForeignKey("self", on_delete = models.CASCADE, related_name = 'folder_FolderFK', null = True, blank = True)
    slug = AutoSlugField(populate_from = 'title', unique = True, editable = True)
    time_registered = models.DateTimeField("Horário Registrado", auto_now_add = True)

    class Meta:
        verbose_name = "Folder"
        verbose_name_plural = "Folders"
        app_label = 'folders'

    def __str__(self):
        return self.title

    def breadcrumbs(self, main):
        breadcrumbs = []
        aux = main
        breadcrumbs.append(main)
        while aux.sub_folder != False:
            if len(breadcrumbs) < 5:
                aux = aux.folder
                breadcrumbs.append(aux)
            else:
                break
        return breadcrumbs