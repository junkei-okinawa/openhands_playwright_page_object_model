import pytest
import allure
from playwright.async_api import Page

from pages.home_page import HomePage

@pytest.mark.asyncio
@allure.epic("Inference Endpoints Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test navigation to Inference Endpoints page")
@allure.description(
    """
    This test verifies:
    1. Inference Endpoints link exists on the home page
    2. Link opens in a new tab
    3. New tab has the correct URL and title
    """
)
@allure.id("20")
async def test_inference_endpoints_navigation(page: Page, home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")

    with allure.step("Verify Inference Endpoints link exists"):
        link = page.locator('xpath=//a[contains(@href,"endpoints.huggingface.co")]')
        await link.wait_for(state="visible")
        assert await link.is_visible()

    with allure.step("Click Inference Endpoints link and wait for new tab"):
        inference_endpoints_page = await home_page.click_inference_endpoints_link()
        
    with allure.step("Verify new tab URL and title"):
        await inference_endpoints_page.wait_for_page_load()
        # URLのドメイン部分を検証
        assert "endpoints.huggingface.co" in inference_endpoints_page.page.url
        title = await inference_endpoints_page.get_page_title()
        assert "Inference Endpoints" in title
