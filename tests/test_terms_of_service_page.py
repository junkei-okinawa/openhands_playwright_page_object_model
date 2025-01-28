import allure
import pytest
from playwright.async_api import Page

from pages.home_page import HomePage


@pytest.mark.asyncio
@allure.epic("Terms Of Service Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test navigation to Terms of service page")
@allure.description(
    """
    This test verifies:
    1. Terms of service link exists in the footer
    2. Clicking the link navigates to the Terms of service page
    3. Terms of service page has the correct title
    """
)
@allure.id("32")
async def test_terms_of_service_page_navigation(page: Page, home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")

    with allure.step("Verify Terms of service link exists in footer"):
        terms_of_service_link = page.locator(
            home_page.locators.TERMS_OF_SERVICE_LINK_FOOTER
        )
        await terms_of_service_link.wait_for(state="visible")
        assert await terms_of_service_link.is_visible()

    with allure.step(
        "Click Terms of service link in footer and wait for Terms of service page to load"
    ):
        terms_of_service_page = await home_page.click_terms_of_service_link_footer()

    with allure.step("Verify Terms of service page title"):
        await terms_of_service_page.wait_for_page_load()
        title = await terms_of_service_page.get_page_title()
        assert "Terms of Service" in title
        assert await terms_of_service_page.verify_title_visible()
