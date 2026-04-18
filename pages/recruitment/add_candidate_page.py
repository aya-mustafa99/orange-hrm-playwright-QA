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
        self.vacancy_input        = page.get_by_label("Vacancy")
        self.contact_number_input = page.get_by_label("Contact Number")
        self.email_input          = page.get_by_label("Email")
        self.consent_checkbox     = page.get_by_label("Consent to keep data")
        self.resume_input         = page.locator('input[type="file"]')
        self.save_button          = page.get_by_role("button", name="Save")

    def upload_resume(self, file_path):
        self.resume_input.set_input_files(file_path)

    def add_candidate(self, candidate: CandidateData):
        self.first_name_input.fill(candidate.first_name)
        self.middle_name_input.fill(candidate.middle_name)
        self.last_name_input.fill(candidate.last_name)

        self.vacancy_input.fill(candidate.vacancy)
        self.page.get_by_role("option", name=candidate.vacancy).click()

        self.contact_number_input.fill(candidate.contact_number)
        self.email_input.fill(candidate.email)
        self.upload_resume(candidate.resume_path)
        self.consent_checkbox.check()
        self.save_button.click()