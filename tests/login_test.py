from playwright.sync_api import expect
from pages.login_page import LoginPage


def test_login(page):

    login_page = LoginPage(page)

    login_page.login("Admin", "admin123")

    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()