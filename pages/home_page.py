from playwright.async_api import Page

from .base_page import BasePage
from .datasets_page import DatasetsPage
from .locators import HomePageLocators
from .models_page import ModelsPage
from .spaces_page import SpacesPage


class HomePage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.models_tab = page.locator(HomePageLocators.MODELS_TAB)

    async def click_models_tab(self):
        await self.models_tab.click()
        return ModelsPage(self.page)

    @property
    def datasets_tab(self):
        return self.page.locator(HomePageLocators.DATASETS_TAB)

    async def click_datasets_tab(self):
        await self.datasets_tab.click()
        return DatasetsPage(self.page)

    @property
    def spaces_tab(self):
        return self.page.locator(HomePageLocators.SPACES_TAB)

    async def click_spaces_tab(self):
        await self.spaces_tab.click()
        return SpacesPage(self.page)

    @property
    def posts_tab(self):
        return self.page.locator(HomePageLocators.POSTS_TAB)

    async def click_posts_tab(self):
        await self.posts_tab.click()

    @property
    def docs_tab(self):
        return self.page.locator(HomePageLocators.DOCS_TAB)

    async def click_docs_tab(self):
        await self.docs_tab.click()

    @property
    def enterprise_tab(self):
        return self.page.locator(HomePageLocators.ENTERPRISE_TAB)

    async def click_enterprise_tab(self):
        await self.enterprise_tab.click()

    @property
    def pricing_tab(self):
        return self.page.locator(HomePageLocators.PRICING_TAB)

    async def click_pricing_tab(self):
        await self.pricing_tab.click()

    async def navigate_to_models_page(self):
        await self.click_models_tab()
        from .models_page import ModelsPage

        return ModelsPage(self.page)
