from folders.models import Folder
import string
import random
from django.template.defaultfilters import slugify

"""
python manage.py shell
exec(open('apps/scripts/register_folders.py').read())
"""

def generate_title():
    for x in range(8):
        text = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    return text

folders = Folder.objects.all()

if len(folders) > 200:
    print("Não há necessidade de registrar novos folders.")
else:
    if not Folder.objects.all().exists():
        Folder(title = generate_title(), sub_folder = False).save()
        folders = Folder.objects.all()

    list_folders = []

    for folder in folders:
        for creating_folder in range(random.randint(15, 50)):
            boolean = random.randint(0,1)

            title = generate_title()

            description = {
                "title": title,
                "sub_folder": boolean,
                "slug": slugify(title),
            }

            if boolean:
                obj_folder = Folder(**description, folder = folder)
            else:
                obj_folder = Folder(**description)
            list_folders.append(obj_folder)
    Folder.objects.bulk_create(list_folders)
