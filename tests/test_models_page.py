import allure
import pytest
import asyncio
from playwright.async_api import Page, expect

from pages.home_page import HomePage

@pytest.mark.asyncio
async def test_navigate_to_models_page(page: Page):
    home_page = HomePage(page)
    models_page = await home_page.navigate_to_models_page()
    title_text = await models_page.get_title_text()
    assert title_text == "Models"


@pytest.mark.asyncio
async def test_search_models(page: Page):
    home_page = HomePage(page)
    models_page = await home_page.navigate_to_models_page()
    await models_page.search_models("bert")
    await expect(models_page.filter_by_name_box).to_have_value("bert")
