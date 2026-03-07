from playwright.sync_api import Page

class AddEmployeePage:

    def __init__(self, page: Page):
        self.page = page

        # menu
        self.pim_menu = page.get_by_role("link", name="PIM")
        self.add_employee_btn = page.get_by_role("link", name="Add Employee")

        # employee name
        self.first_name = page.locator("input[name='firstName']")
        self.middle_name = page.locator("input[name='middleName']")
        self.last_name = page.locator("input[name='lastName']")

        # login details
       
        self.login_details_checkbox = page.locator("input[type='checkbox']")
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.confirm_password_input = page.get_by_label("Confirm Password")
        self.status_enabled = page.get_by_label("Enabled")
        self.status_disabled = page.get_by_label("Disabled")

        # save
        self.save_btn = page.get_by_role("button", name="Save")

    def open_add_employee(self):
        self.pim_menu.wait_for(state="visible", timeout=10000)
        self.pim_menu.click()
        self.page.wait_for_load_state("networkidle") 
        self.add_employee_btn.wait_for(state="visible", timeout=5000)
        self.add_employee_btn.click()

    def fill_employee_name(self, first, middle, last):
        self.first_name.fill(first)
        self.middle_name.fill(middle)
        self.last_name.fill(last)

    def enable_login_details(self):
        self.login_details_checkbox.check()


    def fill_login_details(self, username, password, status_enabled=True):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)
        if status_enabled:
            self.status_enabled.check()
        else:
            self.status_disabled.check()

    def save_employee(self):
        self.save_btn.click()