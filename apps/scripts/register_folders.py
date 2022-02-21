from folders.models import Folder
import string
import random

"""
python manage.py shell
exec(open('apps/scripts/register_folders.py').read())
"""

def generate_title():
    for x in range(8):
        text = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    return text

folders = Folder.objects.all()

if not Folder.objects.all().exists():
    Folder(title = generate_title(), sub_folder = False).save()
    folders = Folder.objects.all()

list_folders = []

for folder in folders:
    for creating_folder in range(random.randint(15, 30)):
        boolean = random.randint(0,1)
        if boolean:
            obj_folder = Folder(title = generate_title(), sub_folder = boolean, folder = folder)
        else:
            obj_folder = Folder(title = generate_title(), sub_folder = boolean)
        list_folders.append(obj_folder)
Folder.objects.bulk_create(list_folders)