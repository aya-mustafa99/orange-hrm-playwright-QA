from playwright.sync_api import expect

class SearchEmployeePage:

    def __init__(self, page):
        self.page = page

        self.employee_name = page.get_by_label("Employee Name")
        self.employee_id = page.get_by_label("Employee Id")
        self.search_btn = page.get_by_role("button", name="Search")
        self.record_found = page.get_by_text("Record Found")
        self.no_records = page.get_by_text("No Records Found")

    def search_by_name(self, name):
        self.employee_name.fill(name)
        self.search_btn.click()

    def search_by_id(self, emp_id):
        self.employee_id.fill(emp_id)
        self.search_btn.click()

    def verify_employee_visible(self, name):
        expect(self.page.get_by_text(name).first).to_be_visible()

    def verify_employee_id_visible(self, emp_id):
        expect(self.page.get_by_text(emp_id).first).to_be_visible()

    def verify_record_found(self):
        expect(self.record_found).to_be_visible()

    def verify_no_records(self):
        expect(self.no_records).to_be_visible()