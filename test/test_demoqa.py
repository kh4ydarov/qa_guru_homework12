import allure

from model.registration_page import RegistrationPage
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Sarvar")
@allure.feature("Задачи в репозиторий")
@allure.story("Регистрация нового пользователя")
@allure.link("https://github.com", name="Testing")

def test_registration_form():
    with allure.step("Open registration form"):
        registration_page = RegistrationPage()
        registration_page.open()

    with allure.step("Fill registration form"):
        registration_page.fill_first_name('John')
        registration_page.fill_last_name('Doe')
        registration_page.fill_email('mail@gmail.com')
        registration_page.fill_gender('Other')
        registration_page.fill_mobile_number('9981111111')
        registration_page.fill_date_of_birth('1999', 'May', '17')
        registration_page.fill_subjects('Maths')
        registration_page.fill_hobbies('Music')
        registration_page.upload_picture('test.jpg')
        registration_page.fill_current_address('test_address')
        registration_page.fill_state('Haryana')
        registration_page.fill_city('Panipat')
        registration_page.submit()

    with allure.step("Checking final page"):
        registration_page.should_registered_user_with(
            'John',
            'Doe',
            'mail@gmail.com',
            'Other',
            '9981111111',
            '17 May,1999',
            'Maths',
            'Music',
            'test.jpg',
            'test_address',
            'Haryana',
            'Panipat'
        )
