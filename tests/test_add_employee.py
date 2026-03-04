from playwright.sync_api import Page, expect
def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="PIM").click()
    page.get_by_role("button", name=" Add").click()
    page.get_by_role("textbox", name="First Name").fill("ayaa")
    page.get_by_role("textbox", name="Middle Name").fill("ayaa")
    page.get_by_role("textbox", name="Last Name").fill("ayaa")
    page.get_by_role("textbox",name="Employee Id").fill("7777777")
    page.get_by_role("button", name="Save").click()
    page.locator("form").filter(has_text="Employee Full NameEmployee").get_by_role("button").click()
    page.get_by_role("link", name="Employee List").click()
    expect(page.get_by_text("ayaa ayaa")).to_be_visible()
    
