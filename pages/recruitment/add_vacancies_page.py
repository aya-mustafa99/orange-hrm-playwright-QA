from dataclasses import dataclass, field
from faker import Faker
from playwright.sync_api import Page

fake = Faker()


@dataclass
class VacancyData:
    vacancy_name: str = field(default_factory=lambda: fake.job())
    job_title: str = "QA Engineer"
    description: str = field(default_factory=fake.text)
    hiring_manager: str = "Admin"
    positions: int = 1
    active: bool = True


class AddVacanciesPage:
    def __init__(self, page: Page):
        self.page = page
        self.vacancy_name_input = page.locator(".oxd-input-group").filter(has_text="Vacancy Name").locator("input")
        self.job_title_input = page.locator(".oxd-input-group").filter(has_text="Job Title").locator(".oxd-select-text-input")
        self.description_input    = page.get_by_role("textbox", name="Type description here")
        self.hiring_manager_input = page.get_by_placeholder("Type for hints...")
        self.positions_input      = page.locator("input[type='number']")
        self.active_toggle        = page.locator("input[type='checkbox']")
        self.save_btn             = page.get_by_role("button", name="Save")

    def get_first_hiring_manager(self) -> str:
      self.hiring_manager_input.fill("A")
      first_option = self.page.get_by_role("option").first
      first_option.wait_for()
      name = first_option.inner_text()
      first_option.dispatch_event("click")
      return name


    def add_vacancy(self, vacancy: VacancyData):
      self.vacancy_name_input.fill(vacancy.vacancy_name)
      self.job_title_input.click()
      self.page.get_by_role("option", name=vacancy.job_title).click()
      self.description_input.fill(vacancy.description)
      vacancy.hiring_manager = self.get_first_hiring_manager()  
      self.positions_input.fill(str(vacancy.positions))
      if vacancy.active:
          if not self.active_toggle.is_checked():
            self.active_toggle.click()
      self.save_btn.click()