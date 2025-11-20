from data.users import student
from model.pages.registration_page import RegistrationPage


def test_registration_form(config_browser):
    registration_page = RegistrationPage()
    registration_page.open()
    # WHEN
    registration_page.registration_form(student)
    # THEN
    registration_page.should_registration_form_user(student)
