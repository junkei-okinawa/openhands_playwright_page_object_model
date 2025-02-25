from playwright.async_api import Page

from .base_page import BasePage
from .locators import PostsPageLocators


class PostsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = PostsPageLocators()

    async def navigate(self):
        await self.page.goto("https://huggingface.co/posts/")
