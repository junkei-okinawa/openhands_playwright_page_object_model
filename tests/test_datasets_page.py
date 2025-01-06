import pytest
import asyncio
from playwright.async_api import Page

from pages.home_page import HomePage
from pages.datasets_page import DatasetsPage

@pytest.mark.asyncio
async def test_datasets_page_title(page: Page):
    home_page = HomePage(page)
    datasets_page = await home_page.click_datasets_tab()
    title_text = await datasets_page.get_title_text()
    assert title_text == "Datasets"
