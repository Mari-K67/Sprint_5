import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import LogInOutLocators
import data

class TestRegistration:
    def test_user_login_successful(self, driver):
        driver.get(data.url_main_page)
        #Нажать кнопку "Вход и регистрация"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LogInOutLocators.login_and_registration_button)).click()

        #Заполнить поля email, пароль
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(LogInOutLocators.email_field))
        driver.find_element(*LogInOutLocators.email_field).send_keys(data.email_exist_user) 
        driver.find_element(*LogInOutLocators.password_field).send_keys(data.password_exist_user)

        #Нажать кнопку "Вход"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LogInOutLocators.login_button)).click()

        #1- произошел переход на произошёл переход на главную страницу;
        current_url = driver.current_url 
        assert current_url == data.url_main_page_after_login

        # 2- отображается аватар пользователя; 
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located(LogInOutLocators.user_photo)).is_displayed()
        
        # 3- имя==User.
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located(LogInOutLocators.user_name)).text == 'User.'

    def test_user_logout_successful(self, driver):
        driver.get(data.url_main_page)
        #Нажать кнопку "Вход и регистрация"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LogInOutLocators.login_and_registration_button)).click()

        #Заполнить поля email, пароль
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(LogInOutLocators.email_field))
        driver.find_element(*LogInOutLocators.email_field).send_keys(data.email_exist_user) 
        driver.find_element(*LogInOutLocators.password_field).send_keys(data.password_exist_user)

        #Нажать кнопку "Вход"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LogInOutLocators.login_button)).click()

        #Нажать кнопку "Выйти"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LogInOutLocators.logout_button)).click()

        #отображается кнопка "Вход и регистрация"
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located(LogInOutLocators.login_and_registration_button)).is_displayed()