import allure
import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.tasks_page import TasksPage


@pytest.mark.asyncio
@allure.epic("Tasks Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test clicking the Tasks link")
@allure.description(
    "This test verifies that clicking the Tasks link navigates to the correct page and displays the expected title."
)
@allure.id("13")
async def test_tasks_page_title(page: Page, home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    with allure.step("Click the Tasks link"):
        tasks_page = await home_page.click_tasks_link()
    with allure.step("Verify the title of the Tasks page"):
        assert "Tasks" in await tasks_page.get_page_title()
