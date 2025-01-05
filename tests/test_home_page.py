import asyncio
from playwright.async_api import async_playwright
from pages.home_page import HomePage
import pytest
from pages.spaces_page import SpacesPage

@pytest.mark.asyncio
async def test_click_models_tab():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://huggingface.co/")
        home_page = HomePage(page)
        models_page = await home_page.click_models_tab()
        title_text = await models_page.get_title_text()
        assert title_text == "Models"
        print("Models tab clicked successfully")
        await page.screenshot(path="tests/screenshots/models_tab.png")
        await browser.close()

@pytest.mark.asyncio
async def test_click_datasets_tab():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://huggingface.co/")
        home_page = HomePage(page)
        datasets_page = await home_page.click_datasets_tab()
        title_text = await datasets_page.get_title_text()
        assert title_text == "Datasets"
        print("Datasets tab clicked successfully")
        await page.screenshot(path="tests/screenshots/datasets_tab.png")
        await browser.close()

@pytest.mark.asyncio
async def test_click_spaces_tab():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://huggingface.co/")
        home_page = HomePage(page)
        spaces_page = await home_page.click_spaces_tab()
        title_text = await spaces_page.get_title_text()
        assert title_text == "Spaces"
        print("Spaces tab clicked successfully")
        await page.screenshot(path="tests/screenshots/spaces_tab.png")
        await browser.close()

@pytest.mark.asyncio
async def test_click_posts_tab():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://huggingface.co/")
        home_page = HomePage(page)
        await home_page.click_posts_tab()
        print("Posts tab clicked successfully")
        await page.screenshot(path="tests/screenshots/posts_tab.png")
        await browser.close()

@pytest.mark.asyncio
async def test_click_docs_tab():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://huggingface.co/")
        home_page = HomePage(page)
        await home_page.click_docs_tab()
        print("Docs tab clicked successfully")
        await page.screenshot(path="tests/screenshots/docs_tab.png")
        await browser.close()

@pytest.mark.asyncio
async def test_click_enterprise_tab():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://huggingface.co/")
        home_page = HomePage(page)
        await home_page.click_enterprise_tab()
        print("Enterprise tab clicked successfully")
        await page.screenshot(path="tests/screenshots/enterprise_tab.png")
        await browser.close()

@pytest.mark.asyncio
async def test_click_pricing_tab():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://huggingface.co/")
        home_page = HomePage(page)
        await home_page.click_pricing_tab()
        print("Pricing tab clicked successfully")
        await page.screenshot(path="tests/screenshots/pricing_tab.png")
        await browser.close()
