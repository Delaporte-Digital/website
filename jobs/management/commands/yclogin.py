from django.core.management.base import BaseCommand, CommandError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import os


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        driver = webdriver.Chrome()
        driver.get("https://www.workatastartup.com/")
        driver.find_element(By.XPATH, "//a[contains(text(),'Log In ›')]").click()
        try:
            # Wait until the username and password fields are present
            wait = WebDriverWait(driver, 10)
            username_field = wait.until(EC.presence_of_element_located((By.ID, 'ycid-input')))
            password_field = wait.until(EC.presence_of_element_located((By.ID, 'password-input')))

            # Enter the login credentials
            username_field.send_keys("rodrigod@delaportedigital.com")
            password_field.send_keys(os.getenv("YC_PASSWORD"))

            # Submit the form
            password_field.submit()

            time.sleep(15)  # Let the user actually see something!
            # Save the session ID and URL
            session_id = driver.session_id
            executor_url = driver.current_url
            with open('session.pkl', 'wb') as f:
                pickle.dump((session_id, executor_url), f)
        finally:
            driver.quit()
        driver.quit()