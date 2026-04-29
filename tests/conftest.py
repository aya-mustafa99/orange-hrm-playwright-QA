import pytest
from faker import Faker
from playwright.sync_api import Page
from pages.login_page import LoginPage

fake = Faker()

@pytest.fixture(scope="function", autouse=True)
def goto(page: Page):
    """Fixture to navigate to the base URL."""
    base_url = "https://opensource-demo.orangehrmlive.com/"
    page.set_default_timeout(100000)
    page.goto(base_url)

@pytest.fixture(autouse=True)
def login(page: Page):
    login_page = LoginPage(page)
    login_page.login("Admin", "admin123")
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
        "email": fake.email(),
        "contact": fake.phone_number(),
        "vacancy": vacancy_data["name"],
        "resume_path": "tests/files/resume.pdf"
    }