from playwright.async_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    async def wait_for_load_state(self):
        await self.page.wait_for_load_state()

    async def goto(self, url: str):
        await self.page.goto(url)
        await self.wait_for_load_state()

