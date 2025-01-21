import pytest
from playwright.sync_api import Page
from pages.docs_page import DocsPage

@pytest.mark.asyncio
@pytest.mark.docs
async def test_docs_page_title(page: Page, base_url):
    docs_page = DocsPage(page)
    await docs_page.navigate()
    assert "Documentation" in await docs_page.get_page_title()
