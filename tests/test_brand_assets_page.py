import allure
import pytest
from playwright.async_api import Page

from pages.home_page import HomePage


@pytest.mark.asyncio
@allure.epic("Brand Assets Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test navigation to Brand assets page")
@allure.description(
    """
    This test verifies:
    1. Brand assets link exists in the footer
    2. Clicking the link navigates to the Brand assets page
    3. Brand assets page has the correct title
    """
)
@allure.id("31")
async def test_brand_assets_page_navigation(page: Page, home_page: HomePage):
    try:
        with allure.step("Navigate to the Hugging Face home page"):
            await home_page.goto("https://huggingface.co/")

        with allure.step("Verify Brand assets link exists in footer"):
            brand_assets_link = page.locator(
                home_page.locators.BRAND_ASSETS_LINK_FOOTER
            )
            await brand_assets_link.wait_for(state="visible")
            assert await brand_assets_link.is_visible()

        with allure.step(
            "Click Brand assets link in footer and wait for Brand assets page to load"
        ):
            brand_assets_page = await home_page.click_brand_assets_link_footer()

        with allure.step("Verify Brand assets page title"):
            await brand_assets_page.wait_for_page_load()
            title = await brand_assets_page.get_page_title()
            assert "Brand assets - Hugging Face" == title
            assert await brand_assets_page.verify_title_visible()
    except Exception as e:
        page_content = await page.content()
        print(f"Page content: {page_content}")
        raise e
