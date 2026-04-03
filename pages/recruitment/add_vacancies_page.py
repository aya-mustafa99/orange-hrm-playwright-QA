
class AddVacancyPage:
    def __init__(self, page):
        self.page = page
        self.vacancy_name = page.get_by_label("Vacancy Name")
        self.job_title = page.get_by_label("Job Title")
        self.description = page.get_by_role("textbox", name="Type description here")
        self.hiring_manager = page.get_by_role("textbox", name="Type for hints...")
        self.positions = page.locator("input[type='number']")
        self.active_toggle = page.locator("input[type='checkbox']")
        self.save_btn = page.get_by_role("button", name="Save")

    def add_vacancy(self, name, job_title, description, manager, positions, active=True):
            self.page.context.tracing.group(f"Add Vacancy: {name}")
            self.vacancy_name.fill(name)
            self.job_title.click()
            self.page.get_by_text(job_title).click()
            self.description.fill(description)
            self.hiring_manager.fill(manager)
            self.positions.fill(str(positions))
            if active:
                if not self.active_toggle.is_checked():
                    self.active_toggle.click()
            self.save_btn.click()