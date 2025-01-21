import pytest
from playwright.sync_api import Page

from pages.enterprise_page import EnterprisePage

import allure
import pytest

@pytest.mark.asyncio
@allure.epic("Enterprise Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("This test verifies that the Enterprise page title is correct.")
@allure.id("13")
@pytest.mark.enterprise
async def test_enterprise_page_title(page: Page, base_url):
    enterprise_page = EnterprisePage(page)
    await enterprise_page.navigate()
    assert "Enterprise" in await enterprise_page.get_page_title()
    await enterprise_page.navigate()