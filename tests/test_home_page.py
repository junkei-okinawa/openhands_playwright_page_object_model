import pytest
import asyncio
from playwright.async_api import Page

from pages.home_page import HomePage
from pages.spaces_page import SpacesPage

@pytest.mark.asyncio
async def test_click_models_tab(page: Page):
    home_page = HomePage(page)
    models_page = await home_page.click_models_tab()
    title_text = await models_page.get_title_text()
    assert title_text == "Models"


@pytest.mark.asyncio
async def test_click_datasets_tab(page: Page):
    home_page = HomePage(page)
    datasets_page = await home_page.click_datasets_tab()
    title_text = await datasets_page.get_title_text()
    assert title_text == "Datasets"


@pytest.mark.asyncio
async def test_click_spaces_tab(page: Page):
    home_page = HomePage(page)
    spaces_page = await home_page.click_spaces_tab()
    title_text = await spaces_page.get_title_text()
    assert title_text == "Spaces"


@pytest.mark.asyncio
async def test_click_posts_tab(page: Page):
    home_page = HomePage(page)
    await home_page.click_posts_tab()


@pytest.mark.asyncio
async def test_click_docs_tab(page: Page):
    home_page = HomePage(page)
    await home_page.click_docs_tab()


@pytest.mark.asyncio
async def test_click_enterprise_tab(page: Page):
    home_page = HomePage(page)
    await home_page.click_enterprise_tab()


@pytest.mark.asyncio
async def test_click_pricing_tab(page: Page):
    home_page = HomePage(page)
    await home_page.click_pricing_tab()


@pytest.mark.asyncio
async def test_failing_test(page: Page):
    assert await page.title() == "Wrong Title"
