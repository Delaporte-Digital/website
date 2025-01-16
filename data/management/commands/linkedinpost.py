from django.core.management.base import BaseCommand, CommandError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep



class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Example usage with headless Chrome:
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')  # Run Chrome in headless mode
        #options.add_argument('--no-sandbox')
        #options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)

        driver.get("https://www.linkedin.com/login")
        try:
            # Wait until the username and password fields are present
            wait = WebDriverWait(driver, 10)
            username_field = wait.until(EC.presence_of_element_located((By.ID, 'username')))
            password_field = wait.until(EC.presence_of_element_located((By.ID, 'password')))

            # Enter the login credentials
            username_field.send_keys("rod.delaporte@gmail.com")
            password_field.send_keys("")

            # Submit the form
            driver.find_element(By.XPATH, "//button[contains(text(),'Sign in')]").click()
        except Exception as e:
            print(e)
        
        post_url = "https://www.linkedin.com/feed/update/urn:li:activity:7193889814536929283/"  # Replace with the actual post URL
        
        driver.get(post_url)

        driver.find_element(By.ID, "ember89").click()
        driver.find_element(By.XPATH, '//h5[contains(text(), "Most recent")]').click()

        # Wait for the comments to load (adjust the timeout as needed)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'section'))
        )

        # Repeatedly click "Load more comments" until all comments are loaded
        # while True:
        #     try:
        #         # Find the "Load more comments" button
        #         load_more_button = WebDriverWait(driver, 10).until(
        #             EC.element_to_be_clickable((By.ID, "ember1687"))  # Replace with the actual button ID
        #         )
        #         load_more_button.click()
        #         sleep(2)  # Wait for comments to load
        #     except TimeoutException:
        #         # If the button is not found, all comments are likely loaded
        #         break
                
        comment_elements = driver.find_elements(By.XPATH, '//*/p')
        for n in comment_elements:
            print(n.text)

        driver.quit()