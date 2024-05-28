 """ VISIT THE URL: https://www.saucedemo.com/     AND LOGIN WITH THE FOLLOWING CREDENTIALS
 Username = standard_user
 Password = secret_sauce

 TRY TO FETCH THE FOLLOWING USING PYTHON SELENIUM:-
 (1) TITLE OF THE WEBPAGE.
 (2) CURRENT URL OF THE WEBPAGE.
 (3) EXTRACT THE ENTIRE CONTENTS OF THE WEBPAGE AND SAVE IT IN A TEXT FILE WHOSE NAME WILL BE "Webpage_task_11.txt" ."""


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webriver.firefox.service import Service
from webdrivermanager.firefox import Geckodrivermanager

class Secret_sauce:
    def sauce_demo:
       try:
             url = 'https://www.saucedemo.com/'
             driver = webdriver.Firefox(service=service(GeckoDriverManager().install()))
             driver.maximize_window()
             driver.get(url)
             sleep(3)
             print(driver.title)
             sleep(3)
             print(driver.current_url)
             
             element_of_name = driver.find_element(By.ID, "user-name")
             element_of_name.send_keys("standard_user")
             
             element_of_first_password = driver.find_element(By.ID, "password")
             element_of_first_password.send_keys("secret_sauce")
             
             webdriver_path = "C:\bin"
             driver.get(url)
             extract_source = driver.page_source
             
             with open('Webpage_task_11.txt', 'w', encoding='utf-8') as file:
                 file.write(extract_source)
             
             driver.quit()
 
        
        print("Webpage is extracted in 'Webpage_task_11.txt':")
      except NoSuchElementException:
        print("Error")
      
    

result = Secret_sauce
result.sauce_demo()


