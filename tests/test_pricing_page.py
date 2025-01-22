import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.pricing_page import PricingPage


import allure

@pytest.mark.asyncio
@allure.epic("Pricing Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test clicking the Pricing tab")
@allure.description(
    "This test verifies that clicking the Pricing tab navigates to the correct page and displays the expected title."
)
@allure.id("9")
async def test_pricing_page_title(page: Page, home_page: HomePage):
    with allure.step("Navigate to the Pricing page"):
        pricing_page = PricingPage(page)
        await home_page.click_pricing_tab()
    with allure.step("Verify the title of the Pricing page"):
        assert "Pricing" in await pricing_page.get_page_title()