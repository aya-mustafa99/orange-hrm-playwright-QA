import pytest
from faker import Faker
from playwright.sync_api import Page
from pages.login_page import LoginPage

fake = Faker()

@pytest.fixture(autouse=True)
def login(page: Page):
    base_url = "https://opensource-demo.orangehrmlive.com/"
    page.set_default_timeout(120000)  
    page.goto(base_url)
    LoginPage(page).login("Admin", "admin123")
    return page

@pytest.fixture
def employee_data():
    first_name = fake.first_name()
    last_name = fake.last_name()
    return {
         "first_name": first_name,
        "last_name": last_name,
        "username": fake.user_name(),
        "full_name":f"{first_name} {last_name}"
    }


@pytest.fixture
def vacancy_data(employee_data):
    return {
        "name": fake.job(),
        "job_title": fake.job(),
        "hiring_manager": employee_data["full_name"]
    }


@pytest.fixture
def candidate_data(vacancy_data):
    return {
        "first_name": fake.first_name(),
        "middle_name": fake.first_name(),
        "last_name": fake.last_name(),
        "vacancy": vacancy_data.name,
        "email": fake.email(),
        "contact": fake.phone_number(),
        "resume_path": "tests/files/resume.pdf"
    }