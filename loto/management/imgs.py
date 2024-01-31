from django.core.management.base import BaseCommand, CommandError

from loto.models import Data, Links

from bs4 import BeautifulSoup
import requests
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        pass
        # parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        # Todo: Get all urls and add a for loop
        # Todo: Get img src link and download img in model fields
        records = Links.objects.all()
        for n in records:
            try:
                r = requests.get(n.url)
                # print(r.content)
                soup = BeautifulSoup(r.text, 'html.parser')
                imgs = soup.find_all('img')
                print(imgs[1].get('src'))
                img1 = requests.get(imgs[1].get('src'))
                img2 = requests.get(imgs[2].get('src'))
                n.resultados.save('img.png', ContentFile(img1.content))
                n.ganadores.save('img.png', ContentFile(img2.content))
            except Exception as e:
                print(e)
