import allure
import pytest
import asyncio
from playwright.async_api import async_playwright, expect
from pages.home_page import HomePage

@pytest.mark.asyncio
async def test_navigate_to_models_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://huggingface.co/")
        home_page = HomePage(page)
        models_page = await home_page.navigate_to_models_page()
        title_text = await models_page.get_title_text()
        assert title_text == "Models"
        png_bytes = await page.screenshot()
        allure.attach(png_bytes, name="models_page", attachment_type=allure.attachment_type.PNG)
        await browser.close()

@pytest.mark.asyncio
async def test_search_models():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://huggingface.co/")
        home_page = HomePage(page)
        models_page = await home_page.navigate_to_models_page()
        await models_page.search_models("bert")
        await expect(models_page.filter_by_name_box).to_have_value("bert")
        
        png_bytes = await page.screenshot()
        allure.attach(png_bytes, name="search_results", attachment_type=allure.attachment_type.PNG)
        await browser.close()
