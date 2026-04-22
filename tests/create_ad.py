import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import CreateAdLocators
from selenium.webdriver.common.by import By 

class TestCreateAd:
    def test_user_without_reqistration_create_ad(self, driver):
        driver.get(CreateAdLocators.url_main_page)
        #Нажать кнопку "Разместить объявление"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(CreateAdLocators.add_ad_button)).click()
        
        #отображается модальное окно с заголовком "Чтобы разместить объявление, авторизуйтесь"
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located(CreateAdLocators.avtorization_request_text)).is_displayed()
        assert WebDriverWait(driver, 3).until(ec.element_to_be_clickable(CreateAdLocators.avtorization_request_text)).text == 'Чтобы разместить объявление, авторизуйтесь'

    def test_user_with_reqistration_create_ad(self, driver):
        driver.get(CreateAdLocators.url_main_page)
        #Нажать кнопку "Вход и регистрация"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(CreateAdLocators.login_and_registration_button)).click()
        
        #Заполнить поля email, пароль
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(CreateAdLocators.email_field))
        driver.find_element(*CreateAdLocators.email_field).send_keys(CreateAdLocators.email_exist_user) 
        driver.find_element(*CreateAdLocators.password_field).send_keys(CreateAdLocators.password_exist_user)

        #Нажать кнопку "Вход"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(CreateAdLocators.login_button)).click()
        
        #для прогрузки страницы
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(CreateAdLocators.user_photo))
        
        #Нажать кнопку "Разместить объявление"
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(CreateAdLocators.add_ad_button)).click()

        #прокрутка страницы
        element = driver.find_element(*CreateAdLocators.name_field)
        driver.execute_script("arguments[0].scrollIntoView();", element)

        #Заполнить поле "Название"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(CreateAdLocators.name_field))
        driver.find_element(*CreateAdLocators.name_field).send_keys(CreateAdLocators.item_name) 

        #Выбрать категорию товара 
        driver.find_element(*CreateAdLocators.drpodown_category).click()
        driver.find_element(*CreateAdLocators.selected_category).click()

        #Выбрать состояние товара
        driver.find_element(*CreateAdLocators.new_or_used).click()

        #Выбрать город
        driver.find_element(*CreateAdLocators.drpodown_city).click()
        driver.find_element(*CreateAdLocators.selected_city).click()

        #Добавить описание товара
        driver.find_element(*CreateAdLocators.item_description_button).send_keys('хорошая книга')

        #Указать стоимость
        driver.find_element(*CreateAdLocators.cost_field).send_keys(1500)

        #Нажать кнопку "Опубликовать"
        driver.find_element(*CreateAdLocators.publish_button).click()

        #в блоке «Мои объявления» отображается созданное объявление
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located(CreateAdLocators.item_name_card)).is_displayed()