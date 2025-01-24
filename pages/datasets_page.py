from playwright.async_api import Page

from .base_page import BasePage
from .locators import DatasetsPageLocators


class DatasetsPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.locators = DatasetsPageLocators()

    @property
    def browse_datasets_button(self):
        return self.locators(DatasetsPageLocators.BROWSE_DATASETS_BUTTON)
