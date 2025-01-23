from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.locators import InferenceEndpointsPageLocators


class InferenceEndpointsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = InferenceEndpointsPageLocators()
