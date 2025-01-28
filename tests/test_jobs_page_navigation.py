import allure
import pytest
from playwright.async_api import Page

from pages.home_page import HomePage


@pytest.mark.asyncio
@allure.epic("Jobs Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test navigation to Jobs page")
@allure.description(
    """
    This test verifies:
    1. Jobs link exists in the footer
    2. Clicking the link opens a new tab
    3. New tab URL contains workable.com
    """
)
@allure.id("34")
async def test_jobs_page_navigation(page: Page, home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")

    with allure.step("Verify Jobs link exists in footer"):
        jobs_link = page.locator(home_page.locators.JOBS_LINK_FOOTER)
        await jobs_link.wait_for(state="visible")
        assert await jobs_link.is_visible()

    with allure.step("Click Jobs link in footer"):
        jobs_page = await home_page.click_jobs_link_footer()

    with allure.step("Verify new tab URL"):
        assert "workable.com" in jobs_page.url