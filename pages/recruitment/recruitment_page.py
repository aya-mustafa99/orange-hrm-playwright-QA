from playwright.sync_api import expect

class RecruitmentPage:

    def __init__(self, page):
        self.page = page
        self.recruitment_menu = page.get_by_role("link", name="Recruitment")
        self.vacancies = page.get_by_role("link", name="Vacancies")

    def go_to_vacancies(self):
        self.recruitment_menu.click()
        self.vacancies.click()