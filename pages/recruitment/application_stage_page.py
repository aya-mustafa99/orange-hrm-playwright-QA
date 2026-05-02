from playwright.sync_api import Page


class ApplicationStagePage:
    def __init__(self, page: Page):
        self.page = page
        self.page_title   = page.locator("h6.orangehrm-main-title")
        self.status_text  = page.locator(".orangehrm-recruitment-status p")
        self.reject_button           = page.get_by_role("button", name="Reject")
        self.shortlist_button        = page.get_by_role("button", name="Shortlist")
        self.save_button             = page.get_by_role("button", name="Save")
        self.interview_button        = page.get_by_role("button", name="Schedule Interview")
        self.mark_passed_button      = page.get_by_role("button", name="Mark Interview Passed")
        self.offer_job_button        = page.get_by_role("button", name="Offer Job")
        self.hire_button             = page.get_by_role("button", name="Hire")
        self.title_input = page.locator("input").nth(0)
        self.date_input = page.locator("input[placeholder='yyyy-dd-mm']")
        self.interviewer_input = page.locator("input[placeholder='Type for hints...']")


    def is_loaded(self) -> bool:
        return self.page_title.inner_text() == "Application Stage"

    def get_status(self) -> str:
        return self.status_text.inner_text()

    def reject(self):
        self.reject_button.click()
        self.save_button.click()

    def shortlist(self):
        self.shortlist_button.click()
        self.save_button.click()  

    def schedule_interview(self):
        self.interview_button.click()
        self.save_button.click()

    def mark_interview_passed(self):
        self.mark_passed_button.click()
        self.save_button.click()

    def offer_job(self):
        self.offer_job_button.click()
        self.save_button.click()

    def hire(self):
        self.hire_button.click()
        self.save_button.click()
    

    def fill_interview(self, title: str, date: str, interviewer: str):
        self.title_input.fill(title)
        self.title_input.press("Tab")
        self.date_input.click()
        self.date_input.fill(date)
        self.date_input.press("Enter")
        self.interviewer_input.click()
        self.interviewer_input.press_sequentially(interviewer, delay=100)
        option = self.page.locator(".oxd-autocomplete-option").first
        option.wait_for(state="visible", timeout=10000)
        option.click()
        self.interviewer_input.press("Tab")