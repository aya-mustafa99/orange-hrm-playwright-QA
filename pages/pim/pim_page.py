from playwright.sync_api import expect

class PimPage:

    def __init__(self, page):
        self.page = page

        self.pim_menu = page.get_by_role("link", name="PIM")
        self.employee_list_menu = page.get_by_role("link", name="Employee List")
        self.add_employee_menu = page.get_by_role("link", name="Add Employee")

    def open_pim(self):
        self.pim_menu.click()

    def open_employee_list(self):
        self.open_pim()
        self.employee_list_menu.click()

    def open_add_employee(self):
        self.open_pim()
        self.add_employee_menu.click()


    def verify_pim_page_open(self):
        expect(self.page.get_by_role("heading", name="PIM")).to_be_visible()