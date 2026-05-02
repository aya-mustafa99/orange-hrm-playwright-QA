from playwright.sync_api import Page


class RecruitmentPage:
    def __init__(self, page: Page):
        self.page = page

        self.recruitment_menu = page.get_by_role("link", name="Recruitment").first
        self.vacancies_tab    = page.get_by_role("link", name="Vacancies")
        self.candidates_tab   = page.get_by_role("link", name="Candidates")
        self.add_button       = page.get_by_role("button", name="Add")

    def navigate(self):
        self.recruitment_menu.click()

    def go_to_vacancies(self):
        self.navigate()
        self.vacancies_tab.click()

    def go_to_candidates(self):
        self.navigate()
        self.candidates_tab.click()

    def go_to_add_vacancy(self):
        self.go_to_vacancies()
        self.add_button.click()

    def go_to_add_candidate(self):
        self.go_to_candidates()
        self.add_button.click()

    def delete_vacancy_by_name(self, name: str):
        self.go_to_vacancies()
        row = self.page.locator("div.oxd-table-row", has_text=name)
        row.get_by_role("button", name="Delete").click()
        self.page.get_by_role("button", name="Yes, Delete").click()

    def delete_candidate_by_name(self, full_name: str):
        self.go_to_candidates()
        row = self.page.locator("div.oxd-table-row", has_text=full_name)
        row.get_by_role("button", name="Delete").click()
        self.page.get_by_role("button", name="Yes, Delete").click()