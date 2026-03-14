import pytest
from pages.pim_page import PimPage
from pages.search_employee import SearchEmployeePage


@pytest.mark.parametrize(
    "search_type,value,expected",
    [
        ("name", "abeer", "found"),
        ("id", "4444", "found"),
        ("name", "wrongname", "not_found"),
        ("id", "99999", "not_found"),
    ],
)

def test_search_employee(login, search_type, value, expected):

    pim_page = PimPage(login)
    search_page = SearchEmployeePage(login)

    pim_page.open_employee_list()

    if search_type == "name":
        search_page.search_by_name(value)
    else:
        search_page.search_by_id(value)

    if expected == "found":
        search_page.verify_record_found()
    else:
        search_page.verify_no_records()