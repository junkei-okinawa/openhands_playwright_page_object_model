from playwright.sync_api import Page
from .base_page import BasePage
from .locators import DocsPageLocators

class DocsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = DocsPageLocators()

    async def navigate(self):
        await self.page.goto("https://huggingface.co/docs")

    async def get_page_title(self):
        return await self.page.title()