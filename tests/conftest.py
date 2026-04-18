import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage


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
    return {
        "first_name": "John",
        "last_name": "Smith",
        "full_name": "John Smith"
    }


@pytest.fixture
def vacancy_data(employee_data):
    return {
        "name": "Automation Engineer",
        "job_title": "QA Engineer",
        "hiring_manager": employee_data["full_name"]
    }


@pytest.fixture
def candidate_data(vacancy_data):
    return {
        "first_name": "Ali",
        "middle_name": "QA",
        "last_name": "Test",
        "email": "ali.test@example.com",
        "contact": "0591234567",
        "vacancy": vacancy_data["name"],
        "resume_path": "tests/files/resume.pdf"
    }