import allure
import pytest
import asyncio
from playwright.async_api import async_playwright, Page

from pages.home_page import HomePage
from pages.datasets_page import DatasetsPage

@pytest.mark.asyncio
async def test_datasets_page_title():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        home_page = HomePage(page)
        await page.goto("https://huggingface.co/")
        datasets_page = await home_page.click_datasets_tab()
        title_text = await datasets_page.get_title_text()
        assert title_text == "Datasets"
        png_bytes = await page.screenshot()
        allure.attach(png_bytes, name="datasets_page", attachment_type=allure.attachment_type.PNG)
