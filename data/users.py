import dataclasses
from dataclasses import dataclass
from datetime import date
from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class Hobby(Enum):
    SPORTS = "Sports"
    READING = "Reading"
    MUSIC = "Music"


@dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    usernumber: str
    birth_month: str
    birth_year: str
    birth_day: str
    subject: str
    picture: str
    address: str
    state: str
    city: str

student = User(first_name='Иван', last_name='Иванов', user_email='ivanov@example.com',
               usernumber='7929100500',birth_month='10',birth_year='1986',birth_day='025',subject='Maths',
               picture='test_image.png',address='Moscow, st.Lenina, 23',state='NCR', city='Delhi')