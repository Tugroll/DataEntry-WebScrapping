from selenium.webdriver.common.by import By
from selenium import webdriver
import time
link_form ="https://forms.gle/LgKm9UvB9pMDHifp9"

class FormBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(chrome_options)
        self.driver.get(link_form)

    def bot_loop(self, soup):
        for current in range(0, len(soup.turn_price_list()) - 1):
            time.sleep(2)
            input_add = self.driver.find_element(By.XPATH,
                                            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            input_add.send_keys(soup.turn_add_list()[current])

            time.sleep(1)
            input_price = self.driver.find_element(By.XPATH,
                                              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            input_price.send_keys(soup.turn_price_list()[current])

            time.sleep(1)
            input_link = self.driver.find_element(By.XPATH,
                                             '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            input_link.send_keys(soup.turn_link_list()[current])

            send_button = self.driver.find_element(By.CSS_SELECTOR, ".Fxmcue")
            send_button.click()
            time.sleep(1)
            go_back_button = self.driver.find_element(By.LINK_TEXT, "Başka bir yanıt gönder")
            go_back_button.click()
            time.sleep(1)
