from playwright.async_api import Page

from .base_page import BasePage
from .locators import ModelsPageLocators

class ModelsPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(ModelsPageLocators.TITLE)

    async def get_title_text(self):
        return await self.title.inner_text()

    @property
    def search_box(self):
        return self.page.locator(ModelsPageLocators.SEARCH_BOX)

    @property
    def see_all_model_results_for_element(self):
        return self.page.locator(ModelsPageLocators.SEE_ALL_MODEL_RESULTS_FOR_ELEMENT)

    @property
    def filter_by_name_box(self):
        return self.page.locator(ModelsPageLocators.FILTER_BY_NAME_BOX)

    async def search_models(self, keyword):
        await self.search_box.wait_for(state="visible")
        await self.search_box.click()
        await self.page.wait_for_load_state()
        await self.search_box.fill(keyword)

        await self.page.wait_for_timeout(1000)
        await self.see_all_model_results_for_element.wait_for()
        await self.see_all_model_results_for_element.click()

    @property
    def first_model_card_title(self):
        return self.page.locator(ModelsPageLocators.FIRST_MODEL_CARD_TITLE)

    async def get_first_model_card_title_text(self):
        return await self.first_model_card_title.inner_text()
