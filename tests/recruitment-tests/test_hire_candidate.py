import pytest
from playwright.sync_api import Page

from pages.recruitment.recruitment_page import RecruitmentPage
from pages.recruitment.add_vacancies_page import AddVacanciesPage, VacancyData
from pages.recruitment.add_candidate_page import AddCandidatePage, CandidateData
from pages.recruitment.application_stage_page import ApplicationStagePage


@pytest.fixture
def setup(page: Page):
    recruitment = RecruitmentPage(page)
    recruitment.go_to_add_vacancy()
    vacancy_data = VacancyData()
    AddVacanciesPage(page).add_vacancy(vacancy_data)
    recruitment.go_to_add_candidate()
    candidate_data = CandidateData(vacancy=vacancy_data.vacancy_name)
    AddCandidatePage(page).add_candidate(candidate_data)
    yield page, candidate_data, vacancy_data
    recruitment = RecruitmentPage(page)
    recruitment.navigate()
    recruitment.delete_candidate_by_name(
        f"{candidate_data.first_name} {candidate_data.last_name}"
    )
    recruitment.go_to_vacancies()
    recruitment.delete_vacancy_by_name(vacancy_data.vacancy_name)


def test_invite_to_interview(setup):
    page, candidate_data, _ = setup
    app_stage = ApplicationStagePage(page)
    assert "Application Initiated" in app_stage.get_status()
    app_stage.shortlist()
    assert "Shortlisted" in app_stage.get_status()
    app_stage.schedule_interview()
    app_stage.fill_interview(
        title="QA Interview",
        date="2026-05-02",
        interviewer="John"
    )
    assert "Interview Scheduled" in app_stage.get_status()



def test_offer_job(setup):
    page, candidate_data, _ = setup
    app_stage = ApplicationStagePage(page)
    assert "Application Initiated" in app_stage.get_status()
    app_stage.shortlist()
    assert "Shortlisted" in app_stage.get_status()
    app_stage.schedule_interview()
    assert "Interview Scheduled" in app_stage.get_status()
    app_stage.mark_interview_passed()
    assert "Interview Passed" in app_stage.get_status()
    app_stage.offer_job()
    assert "Job Offered" in app_stage.get_status()


def test_hire_candidate(setup):
    page, candidate_data, _ = setup
    app_stage = ApplicationStagePage(page)
    assert "Application Initiated" in app_stage.get_status()
    app_stage.shortlist()
    assert "Shortlisted" in app_stage.get_status()
    app_stage.schedule_interview()
    assert "Interview Scheduled" in app_stage.get_status()
    app_stage.mark_interview_passed()
    assert "Interview Passed" in app_stage.get_status()
    app_stage.offer_job()
    assert "Job Offered" in app_stage.get_status()
    app_stage.hire()
    assert "Hired" in app_stage.get_status()