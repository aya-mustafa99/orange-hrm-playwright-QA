from playwright.sync_api import Page, expect
from pages.add_employee_page import AddEmployeePage

class TestAddEmployee:
 def search_employee(self, page, name):
    page.get_by_role("link", name="Employee List").click()
    page.get_by_role("textbox", name="Type for hints...").fill(name)
    page.get_by_role("button", name="Search").click()  

 def test_add_employee_with_login_details(self, page):
    # 1. إنشاء object من AddEmployeePage
    add_emp = AddEmployeePage(page)
    # 2. فتح صفحة Add Employee
    add_emp.open_add_employee()
    # 3. تعبئة بيانات الموظف
    add_emp.fill_employee_name(first="Nada", middle="Moh", last="Salem")
    # 4. تفعيل Login Details
    add_emp.enable_login_details()
    # 5. تعبئة بيانات تسجيل الدخول
    add_emp.fill_login_details(username="nada.moh", password="0000a$m", status_enabled=True)
    # 6. حفظ الموظف
    add_emp.save_employee()
    # 7. تحقق من نجاح الإضافة 
    self.search_employee(page, "Nada")
    expect(page.get_by_text("Nada Moh")).to_be_visible()

 def test_add_employee_without_login_details(self, page):
        add_emp = AddEmployeePage(page)
        add_emp.open_add_employee()
        add_emp.fill_employee_name(first="Lina", middle="Sam", last="Ali")
        add_emp.save_employee()
        self.search_employee(page, "Lina")
        expect(page.get_by_text("Lina Sam")).to_be_visible()
    