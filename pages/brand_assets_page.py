from playwright.async_api import Page, expect

from pages.base_page import BasePage
from pages.locators import BrandAssetsPageLocators


class BrandAssetsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = BrandAssetsPageLocators()

    async def wait_for_page_load(self):
        """
        Wait for the Brand assets page to load
        """
        await self.wait_for_load_state()
        await self.page.wait_for_load_state("domcontentloaded", timeout=60000)

    async def get_page_title(self) -> str:
        """
        Get the page title of the Brand assets page.
        Returns:
            str: The page title
        """
        await self.wait_for_page_load()
        return await self.page.title()

    async def verify_title_visible(self) -> bool:
        """
        Verify the title is visible
        Returns:
            bool: True if title is visible
        """
        await self.title.wait_for(state="visible", timeout=60000)
        return await self.title.is_visible()

    @property
    def title(self):
        """Get page title element"""
        return self.page.locator(self.locators.TITLE)
