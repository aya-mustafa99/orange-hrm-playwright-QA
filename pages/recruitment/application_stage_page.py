from playwright.sync_api import Page
import re


class ApplicationStagePage:
    def __init__(self, page: Page):
        self.page = page

        # Assertion
        self.page_title    = page.locator("h6.orangehrm-main-title")
        self.status_text   = page.locator(".orangehrm-recruitment-status p")

        # Actions
        self.reject_button    = page.get_by_role("button", name="Reject")
        self.shortlist_button = page.get_by_role("button", name="Shortlist")

    def is_loaded(self) -> bool:
     return self.page_title.inner_text() == "Application Stage"

    def get_status(self) -> str:
        return self.status_text.inner_text()

    def reject(self):
        self.reject_button.click()

    def shortlist(self):
        self.shortlist_button.click()