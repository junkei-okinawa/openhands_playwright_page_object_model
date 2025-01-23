from playwright.async_api import Page

from .base_page import BasePage
from .locators import SpacesPageLocators


class SpacesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = SpacesPageLocators()

    async def navigate(self, url: str):
        await self.page.goto("https://huggingface.co/spaces")
