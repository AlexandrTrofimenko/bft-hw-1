from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest


class AudiTestExample(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--remote-allow-origins=*")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_audi_site(self):
        driver = self.driver
        driver.get("https://www.audi.com/en.html")

        time.sleep(5)

        # Проверка 1: Проверить заголовок страницы
        expected_title = "Audi.com – the international Audi website | audi.com"
        actual_title = driver.title
        print(f"Title: {actual_title}")
        self.assertEqual(actual_title, expected_title, "Заголовок страницы не совпадает!")

        # Действие 2: Поиск и проверка текста на главной странице
        header_locator = By.XPATH, '//*[@id="js-page"]/div[4]/div[1]/div/div/div[1]/div[2]/div/h3'
        header_element = driver.find_element(*header_locator)
        self.assertTrue(header_element.is_displayed(), "Заголовок 'Audi A6 Sportback e-tron' не найден!")
        print("Заголовок на странице отображен.")

        # Действие 3: Клик по ссылке "Innovation -> Product Innovation -> Technologies" в меню
        models_tech_locator = By.XPATH, '//*[@id="js-page"]/header/div/nav/div/div[2]/div/ul[1]/li[3]/div/nav/div/ul/li[2]/nav/div/ul/li[3]/div/a[1]'
        models_tech_button = driver.find_element(*models_tech_locator)
        models_tech_button.click()
        time.sleep(5)

        expected_url = "https://www.audi.com/en/innovation/product-innovation/technologies.html"
        current_url = driver.current_url
        print(f"Current URL: {current_url}")
        self.assertEqual(current_url, expected_url, "URL страницы после клика не совпадает!")

        models_page_header_locator = By.XPATH, '//*[@id="js-page"]/div[4]/div[3]/div/div/div[2]'
        models_page_header_element = driver.find_element(*models_page_header_locator)
        self.assertTrue(models_page_header_element.is_displayed(), "Текст Technological leadership is as much a part of the Audi DNA as the iconic four rings. Every day, Audi employees work to ensure that technical progress reaches the road. At the heart of our innovative strength is a unique driving experience. But we go even further: Thanks to future-proof technologies and services, we ensure an unparalleled customer experience. не отображен!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
