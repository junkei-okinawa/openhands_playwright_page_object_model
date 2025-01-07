import pytest
import asyncio
from playwright.async_api import Page

from pages.home_page import HomePage
from pages.spaces_page import SpacesPage


@pytest.mark.asyncio
async def test_click_models_tab(home_page: HomePage, test_data):
    await home_page.goto("https://huggingface.co/")
    tab_data = next(tab for tab in test_data["home_page_tabs"] if tab["tab_name"] == "models")
    models_page = await home_page.click_models_tab()
    title_text = await models_page.get_title_text()
    assert title_text == tab_data["expected_title"]


@pytest.mark.asyncio
async def test_click_datasets_tab(home_page: HomePage, test_data):
    await home_page.goto("https://huggingface.co/")
    tab_data = next(tab for tab in test_data["home_page_tabs"] if tab["tab_name"] == "datasets")
    datasets_page = await home_page.click_datasets_tab()
    title_text = await datasets_page.get_title_text()
    assert title_text == tab_data["expected_title"]


@pytest.mark.asyncio
async def test_click_spaces_tab(home_page: HomePage, test_data):
    await home_page.goto("https://huggingface.co/")
    tab_data = next(tab for tab in test_data["home_page_tabs"] if tab["tab_name"] == "spaces")
    spaces_page = await home_page.click_spaces_tab()
    title_text = await spaces_page.get_title_text()
    assert title_text == tab_data["expected_title"]


@pytest.mark.asyncio
async def test_click_posts_tab(home_page: HomePage):
    await home_page.goto("https://huggingface.co/")
    await home_page.click_posts_tab()


@pytest.mark.asyncio
async def test_click_docs_tab(home_page: HomePage):
    await home_page.goto("https://huggingface.co/")
    await home_page.click_docs_tab()


@pytest.mark.asyncio
async def test_click_enterprise_tab(home_page: HomePage):
    await home_page.goto("https://huggingface.co/")
    await home_page.click_enterprise_tab()


@pytest.mark.asyncio
async def test_click_pricing_tab(home_page: HomePage):
    await home_page.goto("https://huggingface.co/")
    await home_page.click_pricing_tab()


@pytest.mark.asyncio
async def test_failing_test(page: Page):
    assert await page.title() == "Wrong Title"
