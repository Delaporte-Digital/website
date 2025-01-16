from django.core.management.base import BaseCommand, CommandError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run Chrome in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)

        driver.get("https://www.ycombinator.com/companies/industry/api")

        #elements = driver.find_elements(By.XPATH, "//div//ul//a//li")


        #for element in elements:
        spans = driver.find_elements(By.XPATH, '//a//span')

        # for n in spans:
        #     print(n.text)

        

        for n in range(0, len(spans), 7):
            print(spans[n].text)
            print(spans[n+2].text)
            print(spans[n+4].text)
            print(spans[n+6].text)
        # description = driver.find_elements(By.XPATH, '//div[@class="mt-1 line-clamp-3"]')
        # for n in description:
        #     print(n.text)
        # tags = driver.find_elements(By.XPATH, '//div//div[@class="first-of-type:pl-0"]')
        # for n in tags:
        #     print(n.text)
            
        
        
        driver.quit()