from playwright.sync_api import Page

from .base_page import BasePage
from .locators import SpacesPageLocators


class SpacesPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.title = self.page.locator(SpacesPageLocators.TITLE)

    async def get_page_title(self) -> str:
        return await self.title.text_content()