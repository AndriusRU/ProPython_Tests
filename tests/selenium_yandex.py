import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Для linux систем нужно установить соответствующие драйвера в /usr/bin/ и дать права на исполнение
# Скачать для Chrome отсюда http://chromedriver.storage.googleapis.com/index.html
# Статья по решению проблем с драйверами - https://www.pythonfixing.com/2022/04/fixed-webdriverexception-message-not.html
CHROME_DRIVER = ''
LOGIN = 'login'
PASSWORD = 'password'

class TestAuthYandex:

    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.close()

    def test_auth(self):
        self.driver.get("https://passport.yandex.ru/auth")
        time.sleep(3)

        login_in = self.driver.find_element(By.NAME, 'login')
        login_in.send_keys(LOGIN)
        login_in.submit()

        time.sleep(3)

        password_in = self.driver.find_element(By.NAME, 'passwd')
        password_in.send_keys(PASSWORD)
        password_in.submit()


if __name__ == '__main__':
    pytest.main()
