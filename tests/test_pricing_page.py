import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.pricing_page import PricingPage


@pytest.mark.smoke
async def test_pricing_page_title(page: Page, home_page: HomePage):
    pricing_page = PricingPage(page)
    await home_page.click_pricing_tab()
    assert "Pricing" in await pricing_page.get_page_title()