import allure
import pytest
from playwright.async_api import Page

from pages.enterprise_page import EnterprisePage


@pytest.mark.asyncio
@allure.epic("Enterprise Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("This test verifies that the Enterprise page title is correct.")
@allure.id("17")
@pytest.mark.enterprise
async def test_enterprise_page_title(page: Page, base_url):
    with allure.step("Navigate to the Enterprise page"):
        enterprise_page = EnterprisePage(page)
        await enterprise_page.navigate()
    with allure.step("Verify the title of the Enterprise page"):
        assert "Enterprise" in await enterprise_page.get_page_title()
    await enterprise_page.navigate()
