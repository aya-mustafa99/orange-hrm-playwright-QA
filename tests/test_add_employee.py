import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="PIM").click()
    page.get_by_role("button", name=" Add").click()
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("ayaa")
    page.get_by_role("textbox", name="Middle Name").click()
    page.get_by_role("textbox", name="Middle Name").fill("mustafa")
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").fill("qrinawi")
    page.get_by_role("textbox").nth(4).click()
    page.get_by_role("textbox").nth(4).click()
    page.get_by_role("textbox").nth(4).fill("444444")
    page.get_by_role("button", name="Save").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/193")
    expect(page.locator("#app")).to_contain_text("Personal Details")
    expect(page.locator("#app")).to_contain_text("Save")
    page.locator("form").filter(has_text="Employee Full NameEmployee").get_by_role("button").click()
