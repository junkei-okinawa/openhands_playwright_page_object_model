from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.locators import InferenceEndpointsPageLocators

class InferenceEndpointsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = InferenceEndpointsPageLocators()

    async def wait_for_page_load(self):
        """
        Wait for the Inference Endpoints page to load in new tab
        """
        await self.wait_for_load_state()
        # 新しいタブでページが読み込まれるのを待つ
        await self.page.wait_for_load_state("domcontentloaded")

    async def get_page_title(self) -> str:
        """
        Get the page title of the Inference Endpoints page.
        Returns:
            str: The page title
        """
        await self.wait_for_page_load()
        return await self.page.title()
