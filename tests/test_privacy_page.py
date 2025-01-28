import allure
import pytest
from playwright.async_api import Page

from pages.home_page import HomePage


@pytest.mark.asyncio
@allure.epic("Privacy Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test navigation to Privacy page")
@allure.description(
    """
    This test verifies:
    1. Privacy link exists in the footer
    2. Clicking the link navigates to the Privacy page
    3. Privacy page has the correct title
    """
)
@allure.id("33")
async def test_privacy_page_navigation(page: Page, home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")

    with allure.step("Verify Privacy link exists in footer"):
        privacy_link = page.locator(home_page.locators.PRIVACY_LINK_FOOTER)
        await privacy_link.wait_for(state="visible")
        assert await privacy_link.is_visible()

    with allure.step("Click Privacy link in footer and wait for Privacy page to load"):
        privacy_page = await home_page.click_privacy_link_footer()

    with allure.step("Verify Privacy page title"):
        await privacy_page.wait_for_page_load()
        title = await privacy_page.get_page_title()
        assert "Privacy Policy" in title
        assert await privacy_page.verify_title_visible()