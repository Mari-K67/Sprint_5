# Sprint_5
UI testing.

Task: write UI autotests for the educational service [«Доска»](https://qa-desk.education-services.ru).  
Imagine that a manual tester handed you scenarios. They need to be covered with autotests.

## Stage 1. Preparation
- Browser `Chrome` is installed.
- Selenium is connected.

## Stage 2. Study of test scenarios
### User registration
What you need to do:
* Click the "Вход и регистрация" button.
* Click the "Нет аккаунта" button.
* Fill in all fields of the registration form and click the "Создать аккаунт" button.

**Check**: transition to the home page occurred, in the upper right corner next to the "Разместить объявление" button, the user's avatar and name User are displayed.

### User registration with email not matching the pattern `*******@*******.***`
What you need to do: 
* Click the "Вход и регистрация" button.
* Click the "Нет аккаунта" button.
* Fill in the Email field of the registration form and click the "Создать аккаунт" button.

**Check**: the Email, "Пароль", "Повторите пароль" fields are highlighted in red, below the Email field a message "Ошибка" is displayed.

### Registration of an already existing user
What you need to do: 
* Click the "Вход и регистрация" button.
* Click the "Нет аккаунта" button.
* Fill in all fields of the registration form with data of a user already existing in the system and click the "Создать аккаунт" button.

**Check**: the Email, "Пароль", "Повторите пароль" fields are highlighted in red, below the Email field a message "Ошибка" is displayed.

### User login
What you need to do: 
* Click the "Вход и регистрация" button.
* Fill in all fields of the authorization form and click the "Войти" button.

**Check**: transition to the home page occurred, in the upper right corner next to the "Разместить объявление" button, the user's avatar and name User are displayed.

### User logout
What you need to do: 
* Log in as a pre-created user.
* Click the "Выйти" button.

**Check**: the user's avatar and name User are no longer displayed in the upper right corner next to the "Разместить объявление" button, the "Вход и регистрация" button is now displayed there.

### Creating a listing by an unauthorized user
What you need to do: 
* Click the "Разместить объявление" button.

**Check**: a modal window with the title "Чтобы разместить объявление, авторизуйтесь" is displayed.

### Creating a listing by an authorized user
What you need to do: 
* Log in as a pre-created user.
* Fill in all form fields: "Название", "Описание товара", "Стоимость" — the cost must be specified in numeric format.
* Select the "Категорию" and "Город" from the Dropdown.
* Select the "Состояние товара" RadioButton.
* Click the "Опубликовать" button.
* Go to the user's profile.

**Check**: the created listing is displayed in the "Мои объявления" block.

## Stage 3. Preparation of element locators

Determine and describe the necessary locators that you will use in the tests. Use the `locators` module to store locators. 
The locator with the search method should be written to a variable or constant. Variable and constant names should be clear so that it is convenient to work with them.

## Stage 4. Writing tests on Selenium
Check that the tests run. They should pass in at least one browser. You need to send the tests for review with `Google Chrome` connected.  
Each test should be autonomous. This means it opens the page in the browser, performs its task, and closes the browser. Use the `driver.quit()` command at the end of each test.  
The driver instance should be raised and closed either in a fixture or in `setup/teardown` methods.  
A test report is not required.
