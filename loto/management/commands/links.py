from django.core.management.base import BaseCommand, CommandError
import requests
from bs4 import BeautifulSoup

from loto.models import Links


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        pass
        # parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        # counter = 9
        # 
        
        #     r = requests.get(url)
        #     soup = BeautifulSoup(r.text, 'html.parser')
        #     posts = soup.find_all('div',class_="post")
        #     for n in posts:
        #         link = n.findChildren("a").get('src')
        #         print(link)
        #     counter +=1
        counter = 11
        url = 'https://resultadoslotochile.com/resultados-loto/page/{counter}/'.format(counter)
        while counter <= 180:
            try:
                r = requests.get(url)
                soup = BeautifulSoup(r.text, 'html.parser')
                posts = soup.find_all('div',class_="post")
                for n in posts:
                    try:
                        link = n.findChildren("a")
                        print(link[0].get('href'))
                        Links.objects.create(link=link[0].get('href'))
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)
            counter += 1
