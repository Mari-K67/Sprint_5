import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import RegistrationLocators
import data
import helpers

class TestRegistration:
    def test_user_registration_successful(self, driver):
        driver.get(data.url_main_page)
        password = helpers.generate_valid_password()
        #Нажать кнопку "Вход и регистрация"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(RegistrationLocators.login_and_registration_button)).click()

        #Нажать кнопку "Нет аккаунта"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(RegistrationLocators.no_account_button)).click()

        #Заполнить поля email, пароль, повтор пароля
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(RegistrationLocators.email_field))
        driver.find_element(*RegistrationLocators.email_field).send_keys(helpers.generate_valid_email()) 
        driver.find_element(*RegistrationLocators.password_field).send_keys(password)
        driver.find_element(*RegistrationLocators.password_confirmation_field).send_keys(password)

        #Нажать кнопку "Создать аккаунт"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(RegistrationLocators.create_account_button)).click()

        #Проверки:
        # 1- произошел переход на произошёл переход на главную страницу;
        current_url = driver.current_url 
        assert current_url == data.url_main_page_after_registration
        # 2- отображается аватар пользователя; 
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located(RegistrationLocators.user_photo)).is_displayed()
        # 3- имя==User.
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located(RegistrationLocators.user_name)).text == 'User.'

    def test_user_registration_with_invalid_email(self, driver):
        driver.get(data.url_main_page)
        password = helpers.generate_valid_password()
        #Нажать кнопку "Вход и регистрация"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(RegistrationLocators.login_and_registration_button)).click()

        #Нажать кнопку "Нет аккаунта"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(RegistrationLocators.no_account_button)).click()

        #Заполнить поля email, пароль, повтор пароля
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(RegistrationLocators.email_field))
        driver.find_element(*RegistrationLocators.email_field).send_keys(helpers.generate_invalid_email()) 
        driver.find_element(*RegistrationLocators.password_field).send_keys(password)
        driver.find_element(*RegistrationLocators.password_confirmation_field).send_keys(password)

        #Нажать кнопку "Создать аккаунт"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(RegistrationLocators.create_account_button)).click()

        #Проверки: 
        # 1- поля Email, «Пароль», «Повторите пароль» выделены красным
        email_wrapper = WebDriverWait(driver, 3).until(ec.presence_of_element_located(RegistrationLocators.email_error_field))
        border_color_email = email_wrapper.value_of_css_property("border")
        
        password_wrapper = WebDriverWait(driver, 3).until(ec.presence_of_element_located(RegistrationLocators.password_error_field))
        border_color_password = password_wrapper.value_of_css_property("border")
        
        password_confirmation_wrapper = WebDriverWait(driver, 3).until(ec.presence_of_element_located(RegistrationLocators.password_confirmation_error_field))
        border_color_password_confirmation = password_confirmation_wrapper.value_of_css_property("border")
        
        assert "1px solid rgb(255, 105, 114)" in border_color_email
        assert "1px solid rgb(255, 105, 114)" in border_color_password
        assert "1px solid rgb(255, 105, 114)" in border_color_password_confirmation

        # 2- сообщение «Ошибка» под полем Email
        assert driver.find_element(*RegistrationLocators.email_error_word).text == "Ошибка"

    def test_user_registration_with_exist_user(self, driver):
        driver.get(data.url_main_page)
        #Нажать кнопку "Вход и регистрация"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(RegistrationLocators.login_and_registration_button)).click()

        #Нажать кнопку "Нет аккаунта"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(RegistrationLocators.no_account_button)).click()

        #Заполнить поля email, пароль, повтор пароля
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(RegistrationLocators.email_field))
        driver.find_element(*RegistrationLocators.email_field).send_keys(data.email_exist_user) 
        driver.find_element(*RegistrationLocators.password_field).send_keys(data.password_exist_user)
        driver.find_element(*RegistrationLocators.password_confirmation_field).send_keys(data.password_exist_user)

        #Нажать кнопку "Создать аккаунт"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(RegistrationLocators.create_account_button)).click()

        #Проверки: 
        # 1- поля Email, «Пароль», «Повторите пароль» выделены красным
        email_wrapper = WebDriverWait(driver, 3).until(ec.presence_of_element_located(RegistrationLocators.email_error_field))
        border_color_email = email_wrapper.value_of_css_property("border")

        password_wrapper = WebDriverWait(driver, 3).until(ec.presence_of_element_located(RegistrationLocators.password_error_field))
        border_color_password = password_wrapper.value_of_css_property("border")

        password_confirmation_wrapper = WebDriverWait(driver, 3).until(ec.presence_of_element_located(RegistrationLocators.password_confirmation_error_field))
        border_color_password_confirmation = password_confirmation_wrapper.value_of_css_property("border")
        
        assert "1px solid rgb(255, 105, 114)" in border_color_email
        assert "1px solid rgb(255, 105, 114)" in border_color_password
        assert "1px solid rgb(255, 105, 114)" in border_color_password_confirmation

        # 2- сообщение «Ошибка» под полем Email
        assert driver.find_element(*RegistrationLocators.email_error_word).text == "Ошибка"