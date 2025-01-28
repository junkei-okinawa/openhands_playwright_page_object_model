import allure
import pytest
from playwright.async_api import Page

from pages.home_page import HomePage


@pytest.mark.asyncio
@allure.epic("About Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test navigation to About page")
@allure.description(
    """
    This test verifies:
    1. About link exists in the footer
    2. Clicking the link navigates to the About page
    3. About page has the correct title
    """
)
@allure.id("30")
async def test_about_page_navigation(page: Page, home_page: HomePage):
    try:
        with allure.step("Navigate to the Hugging Face home page"):
            await home_page.goto("https://huggingface.co/")

        with allure.step("Verify About link exists in footer"):
            about_link = page.locator(home_page.locators.ABOUT_LINK_FOOTER)
            await about_link.wait_for(state="visible")
            assert await about_link.is_visible()

        with allure.step("Click About link in footer and wait for About page to load"):
            about_page = await home_page.click_about_link_footer()

        with allure.step("Verify About page title"):
            await about_page.wait_for_page_load()
            title = await about_page.get_page_title()
            assert "huggingface (Hugging Face)" == title
            assert await about_page.verify_title_visible()
    except Exception as e:
        page_content = await page.content()
        print(f"Page content: {page_content[:500]}...")  # 最初の500文字だけ表示
        raise e