from playwright.sync_api import Page, expect
from pages.add_employee_page import AddEmployeePage

def test_add_employee_with_login_details(page: Page):
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
    page.get_by_role("link", name="Employee List").click()
    page.get_by_role("textbox", name="Type for hints...").fill("Nada")
    page.get_by_role("button", name="Search").click()
    expect(page.get_by_text("Nada Moh")).to_be_visible()