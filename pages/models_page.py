from playwright.async_api import Page

class ModelsPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('h1')

    async def get_title_text(self):
        return await self.title.inner_text()

    @property
    def search_box(self):
        return self.page.locator('input[placeholder^="Search models"]')

    async def search_models(self, keyword):
        await self.search_box.wait_for(state="visible")
        await self.search_box.fill(keyword)
        await self.page.wait_for_load_state()
        await self.search_box.press("Enter")

    @property
    def first_model_card_title(self):
        return self.page.locator('article:first-child h4')

    async def get_first_model_card_title_text(self):
        return await self.first_model_card_title.inner_text()