from dataclasses import dataclass, field
from faker import Faker
from playwright.sync_api import Page

fake = Faker()


@dataclass
class CandidateData:
    first_name: str = field(default_factory=fake.first_name)
    middle_name: str = field(default_factory=fake.first_name)
    last_name: str = field(default_factory=fake.last_name)
    vacancy: str = ""
    contact_number: str = field(default_factory=lambda: fake.numerify("059#######"))
    email: str = field(default_factory=fake.email)
    resume_path: str = "tests/files/resume.pdf"  


class AddCandidatePage:
    def __init__(self, page: Page):
        self.page = page

        self.first_name_input     = page.get_by_placeholder("First Name")
        self.middle_name_input    = page.get_by_placeholder("Middle Name")
        self.last_name_input      = page.get_by_placeholder("Last Name")
        self.vacancy_input = page.locator(".oxd-select-text-input")  
        self.email_input = self.page.locator("input[placeholder='Type here']").nth(0)    
        self.contact_number_input = self.page.locator("input[placeholder='Type here']").nth(1)   
        self.resume_input         = page.locator('input[type="file"]')
        self.save_button          = page.get_by_role("button", name="Save")

    def select_vacancy(self, vacancy_name: str):
      self.vacancy_input.click()
      option = self.page.locator(".oxd-select-option") .filter(has_text=vacancy_name) .first
      option.wait_for(state="visible", timeout=10000)
      option.click()

    def upload_resume(self, file_path):
        self.resume_input.set_input_files(file_path)

    def add_candidate(self, candidate: CandidateData):
      self.first_name_input.fill(candidate.first_name)
      self.middle_name_input.fill(candidate.middle_name)
      self.last_name_input.fill(candidate.last_name)
      self.select_vacancy(candidate.vacancy)
      self.email_input.fill(candidate.email)
      self.contact_number_input.fill(candidate.contact_number)
      self.upload_resume(candidate.resume_path)
      self.save_button.click()