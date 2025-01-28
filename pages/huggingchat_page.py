from playwright.async_api import Page

from .base_page import BasePage
from .locators import HuggingChatPageLocators


class HuggingChatPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.locators = HuggingChatPageLocators

    @property
    def title(self):
        return self.page.locator(self.locators.TITLE)

    @property
    def chat_input(self):
        return self.page.locator(self.locators.CHAT_INPUT)

    @property
    def new_chat_button(self):
        return self.page.locator(self.locators.NEW_CHAT_BUTTON)

    async def get_title_text(self) -> str:
        return await self.title.text_content()

    async def is_chat_input_visible(self) -> bool:
        return await self.chat_input.is_visible()

    async def is_new_chat_button_visible(self) -> bool:
        return await self.new_chat_button.is_visible()
