from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.locators import PricingPageLocators


class PricingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = PricingPageLocators()

    async def navigate(self, url: str):
        await self.page.goto("https://huggingface.co/pricing")
