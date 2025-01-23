from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.locators import TasksPageLocators


class TasksPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = TasksPageLocators()
