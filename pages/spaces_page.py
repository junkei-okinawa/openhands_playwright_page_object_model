from playwright.async_api import Page

from .base_page import BasePage
from .locators import SpacesPageLocators


class SpacesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = SpacesPageLocators()
        self.title = page.locator(self.locators.TITLE)

    async def get_page_title(self) -> str:
        return await self.title.text_content()
