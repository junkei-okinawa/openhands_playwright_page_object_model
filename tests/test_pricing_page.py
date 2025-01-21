import pytest
from playwright.sync_api import Page
from pages.pricing_page import PricingPage

@pytest.mark.smoke
async def test_pricing_page_title(page: Page):
    pricing_page = PricingPage(page)
    await pricing_page.navigate("https://huggingface.co/pricing")
    assert "Pricing" in await pricing_page.get_page_title()