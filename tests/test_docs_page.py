import allure
import pytest
from playwright.async_api import Page

from pages.docs_page import DocsPage


@pytest.mark.asyncio
@allure.epic("Docs Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("This test verifies that the Docs page title is correct.")
@allure.id("14")
@pytest.mark.docs
async def test_docs_page_title(page: Page, base_url):
    with allure.step("Navigate to the Docs page"):
        docs_page = DocsPage(page)
        await docs_page.navigate()
    with allure.step("Verify the title of the Docs page"):
        assert "Documentation" in await docs_page.get_page_title()
    await docs_page.navigate()
