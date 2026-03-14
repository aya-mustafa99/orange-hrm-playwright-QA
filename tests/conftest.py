import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage


@pytest.fixture(scope="function", autouse=True)
def goto(page: Page):
    """Fixture to navigate to the base URL."""
    base_url = "https://opensource-demo.orangehrmlive.com/"
    page.goto(base_url)

@pytest.fixture
def login(page: Page):
    login_page = LoginPage(page)
    login_page.login("Admin", "admin123")
    return page