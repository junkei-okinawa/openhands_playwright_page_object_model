from playwright.sync_api import Page

from .base_page import BasePage
from .locators import DatasetsPageLocators

class DatasetsPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(DatasetsPageLocators.TITLE)

    async def get_title_text(self) -> str:
        return await self.title.inner_text()


    @property
    def browse_datasets_button(self):
        return self.page.locator(DatasetsPageLocators.BROWSE_DATASETS_BUTTON)

    async def click_browse_datasets_button(self):
        await self.browse_datasets_button.click()
