import pytest
from playwright.sync_api import Page

from pages.enterprise_page import EnterprisePage


@pytest.mark.asyncio
@pytest.mark.enterprise
async def test_enterprise_page_title(page: Page, base_url):
    enterprise_page = EnterprisePage(page)
    await enterprise_page.navigate()
