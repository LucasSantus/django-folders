from django.db import models
from django.template.defaultfilters import slugify

class Folder(models.Model):
    title = models.CharField("title", max_length = 120)
    sub_folder = models.BooleanField(default = False, null = True, blank = True)
    folder = models.ForeignKey("self", on_delete = models.CASCADE, related_name = 'folder_FolderFK', null = True, blank = True)
    slug = models.SlugField(unique = True, null = True, blank = True)
    time_registered = models.DateTimeField("Horário Registrado", auto_now_add = True)

    class Meta:
        verbose_name = "Folder"
        verbose_name_plural = "Folders"
        app_label = 'folders'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)