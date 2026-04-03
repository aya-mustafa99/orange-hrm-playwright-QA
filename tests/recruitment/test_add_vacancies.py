import pytest
from pages.recruitment.recruitment_page import RecruitmentPage
from pages.recruitment.add_vacancies_page import AddVacancyPage


vacancies_data = [
    {"name": "Junior Software Engineer", "job_title": "Software Engineer", "description": "Looking for a junior software engineer with Python skills", "manager": "Richard", "positions": 2,"active": False},
    {"name": "Qa engineer", "job_title": "QA Engineer", "description": "Seeking a QA engineer experienced in Playwright and Python.", "manager": "Richard", "positions": 1,"active": True},
    {"name": "Senior HR Manager", "job_title": "HR Manager", "description": "Experienced HR Manager to lead recruitment operations.", "manager": "Richard", "positions": 3,"active": True},
]


@pytest.fixture
def add_vacancy_page(page):
    recruitment = RecruitmentPage(page)
    recruitment.go_to_vacancies()
    yield AddVacancyPage(page)
    recruitment.go_to_vacancies()
   


@pytest.mark.parametrize("vacancy_data", vacancies_data)
def test_add_vacancy(add_vacancy_page, vacancy_data):
    add_vacancy_page.add_vacancy(
        name=vacancy_data["name"],
        job_title=vacancy_data["job_title"],
        description=vacancy_data["description"],
        manager=vacancy_data["manager"],
        positions=vacancy_data["positions"],
        active=vacancy_data["active"]
    )