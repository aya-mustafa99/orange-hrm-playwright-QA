import pytest
from playwright.sync_api import Page
from pages.recruitment.recruitment_page import RecruitmentPage
from pages.recruitment.add_vacancies_page import AddVacanciesPage, VacancyData


vacancies_data = [
    VacancyData(vacancy_name="Junior Software Engineer", job_title="Software Engineer",
                description="Looking for a junior software engineer with Python skills",
                positions=2, active=False),
    VacancyData(vacancy_name="QA Engineer", job_title="QA Engineer",
                description="Seeking a QA engineer experienced in Playwright and Python.",
                positions=1, active=True),
    VacancyData(vacancy_name="Senior HR Manager", job_title="HR Manager",
                description="Experienced HR Manager to lead recruitment operations.",
                positions=3, active=True),
]


@pytest.fixture
def add_vacancy_page(page: Page):
    recruitment = RecruitmentPage(page)
    recruitment.go_to_add_vacancy() 
    vacancy_data_created = []  
    yield AddVacanciesPage(page), vacancy_data_created
    for vacancy in vacancy_data_created:
        recruitment.delete_vacancy_by_name(vacancy.vacancy_name)
   

@pytest.mark.parametrize("vacancy_data", vacancies_data)
def test_add_vacancy(add_vacancy_page, vacancy_data: VacancyData):
    page_obj, created = add_vacancy_page
    page_obj.add_vacancy(vacancy_data)
    created.append(vacancy_data) 





    