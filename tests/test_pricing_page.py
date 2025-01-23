import allure
import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.pricing_page import PricingPage


@pytest.mark.asyncio
@allure.epic("Pricing Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test clicking the Pricing tab")
@allure.description(
    "This test verifies that clicking the Pricing tab navigates to the correct page and displays the expected title."
)
@allure.id("19")
async def test_pricing_page_title(page: Page, home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    with allure.step("Click the Pricing link"):
        pricing_page = await home_page.click_pricing_tab()
    with allure.step("Verify the title of the Pricing page"):
        assert "Hugging Face – Pricing" in await pricing_page.page.title()
