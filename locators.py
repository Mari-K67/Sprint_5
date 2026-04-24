from selenium.webdriver.common.by import By

class RegistrationLocators:
    #кнопка "Вход и регистрация"
    login_and_registration_button = By.XPATH, "//button[contains(text(), 'Вход и регистрация')]"

    #кнопка "Нет аккаунта"
    no_account_button = By.XPATH, "//button[contains(text(), 'Нет аккаунта')]"

    #поле "Email"
    email_field = By.NAME, "email"

    #поле "Пароль"
    password_field = By.NAME, "password"

    #поле "Повторите пароль"
    password_confirmation_field = By.NAME, "submitPassword"

    #кнопка "Создать аккаунт"
    create_account_button = By.XPATH, "//button[contains(text(), 'Создать аккаунт')]"
    
    #Фотка в профиле
    user_photo = By.XPATH, '//button[@class="circleSmall"]'

    #Имя пользователя (User.)
    user_name = By.XPATH, "//h3[@class='profileText name']"

    #поле "Email" с ошибкой красное
    email_error_field = By.XPATH, "//input[@name='email']//ancestor::div[contains(@class, 'input_inputError')]"

    #поле "Пароль" с ошибкой красное
    password_error_field = By.XPATH, "//input[@name='password']//ancestor::div[contains(@class, 'input_inputError')]"

    #поле "Повторите пароль" с ошибкой красное 
    password_confirmation_error_field = By.XPATH, "//input[@name='submitPassword']//ancestor::div[contains(@class, 'input_inputError')]"

    #Слово "Ошибка" под полем email
    email_error_word = By.CSS_SELECTOR, ".input_span__yWPqB"

class LogInOutLocators:
    #кнопка "Вход и регистрация"
    login_and_registration_button = By.XPATH, "//button[contains(text(), 'Вход и регистрация')]"

    #поле "Email"
    email_field = By.NAME, "email"

    #поле "Пароль"
    password_field = By.NAME, "password"

    #кнопка "Войти"
    login_button = By.XPATH, "//button[@type='submit' and contains(text(), 'Войти')]"

    #Фотка в профиле
    user_photo = By.XPATH, '//button[@class="circleSmall"]'

    #Имя пользователя (User.)
    user_name = By.XPATH, "//h3[@class='profileText name']"

    #кнопка "Выйти"
    logout_button = By.XPATH, "//button[text()='Выйти']"

class CreateAdLocators:
    #кнопка "Вход и регистрация"
    login_and_registration_button = By.XPATH, "//button[contains(text(), 'Вход и регистрация')]"

    #поле "Email"
    email_field = By.NAME, "email"

    #поле "Пароль"
    password_field = By.NAME, "password"

    #кнопка "Войти"
    login_button = By.XPATH, "//button[@type='submit' and contains(text(), 'Войти')]"

    #для прогрузки страницы
    user_photo = By.XPATH, '//button[@class="circleSmall"]'

    #кнопка "Разместить объявление"
    add_ad_button = By.XPATH, "//button[text()='Разместить объявление']"

    #Страница авторизации с заголовком 'Чтобы разместить объявление, авторизуйтесь'
    avtorization_request_text = By.CSS_SELECTOR, "h1.h1"

    #поле "Название"
    name_field = By.XPATH, "//input[@name='name']"

    #Drpodown "Категория"
    drpodown_category = By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrowDown')])[1]"
    
    #выбрать категорию
    selected_category = By.XPATH, "//span[text()='Книги']"

    #состояние товара 
    new_or_used = By.XPATH, "//div[contains(@class, 'radioUnput_inputRegular')]"

    #Dropdown "Город"
    drpodown_city = By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrowDown')])[2]"

    #выбрать город 
    selected_city = By.XPATH, "//span[text()='Нижний Новгород']/ancestor::button"

    #поле "Описание товара"
    item_description_button = By.XPATH, "//textarea[@name='description']"

    #поле "Стоимость"
    cost_field = By.XPATH, "//input[@name='price']"

    #кнопка "Опубликовать"
    publish_button = By.XPATH, "//button[text()='Опубликовать']"
    
    #поиск карточки по названию 
    item_name_card = By.XPATH, "//h2[text()='Бездна Челенджера']"