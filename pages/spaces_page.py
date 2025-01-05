from playwright.async_api import Page

class SpacesPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('h1')

    async def get_title_text(self) -> str:
        return await self.title.text_content()