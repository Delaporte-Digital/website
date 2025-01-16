from django.core.management.base import BaseCommand, CommandError
from selenium import webdriver
import pickle
import time

class Command(BaseCommand):
    help = "Reuses an active session"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('session.pkl', 'rb') as f:
            session_id, executor_url = pickle.load(f)
        
        # Debug statements to check the loaded values
        print(f"Loaded session_id: {session_id}")
        print(f"Loaded executor_url: {executor_url}")

        # Ensure session_id and executor_url are strings
        if not isinstance(session_id, str) or not isinstance(executor_url, str):
            raise ValueError("session_id and executor_url must be strings")

        print(f"Driver session_id: {session_id} (type: {type(session_id)})")
        print(f"Driver executor_url: {executor_url} (type: {type(executor_url)})")
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver = webdriver.Remote(command_executor=executor_url, options=options)
        driver.session_id = session_id

        # Now you can use the driver with the active session
        driver.get("https://www.workatastartup.com/")

        # Perform any actions with the active session
        time.sleep(5)  # Let the user actually see something!

        driver.quit()