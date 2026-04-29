from playwright.sync_api import expect
from pages.pim.pim_page import PimPage

def test_open_employee_list(login):
    pim_page = PimPage(login)
    pim_page.open_employee_list()
    expect(pim_page.page.get_by_role("heading", name="Employee List")).to_be_visible()


def test_open_add_employee(login):
    pim_page = PimPage(login)
    pim_page.open_add_employee()
    expect(pim_page.page.get_by_role("heading", name="Add Employee")).to_be_visible()