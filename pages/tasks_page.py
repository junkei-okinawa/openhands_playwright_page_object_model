from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.locators import TasksPageLocators


class TasksPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = TasksPageLocators()
        self.title = page.locator(self.locators.TITLE)

    async def get_page_title(self) -> str:
        return await self.title.text_content()
