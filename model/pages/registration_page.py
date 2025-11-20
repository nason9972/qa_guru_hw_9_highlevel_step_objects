import os
from selene import browser, have, be

from data.users import student, User


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('label[for="gender-radio-1"]')
        self.user_number = browser.element('#userNumber')
        self.birth = browser.element('#dateOfBirthInput')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.element('label[for="hobbies-checkbox-1"]')
        self.upload_picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit = browser.element('#submit')
        self.table = browser.all('.table td')

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def registration_form(self, user: User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.user_email)
        self.gender.click()
        self.user_number.type(user.usernumber)
        self.birth.click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'option[value="{user.birth_month}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'option[value="{user.birth_year}"]').click()
        browser.element(f'.react-datepicker__day--{user.birth_day}').click()
        self.subjects.type(user.subject).press_enter()
        self.hobbies.click()
        self.upload_picture.set_value(os.path.abspath(f'../test_data/{user.picture}'))
        self.address.type(user.address)
        self.state.click()
        browser.element('#react-select-3-input').type(user.state).press_enter()
        self.city.click()
        browser.element('#react-select-4-input').type(user.city).press_enter()
        self.submit.click()
        return self

    def should_registration_form_user(self, user: User):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        self.table.should(have.exact_texts(
            'Student Name', f'{user.first_name} {user.last_name}',
            'Student Email', user.user_email,
            'Gender', 'Male',
            'Mobile', user.usernumber,
            'Date of Birth', '25 November,1986',
            'Subjects', user.subject,
            'Hobbies', 'Sports',
            'Picture', user.picture,
            'Address', user.address,
            'State and City', f'{user.state} {user.city}'
        ))
        return self
