import asyncio
from playwright.async_api import async_playwright
import pytest

@pytest.mark.asyncio
async def test_example():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        title = await page.title()
        assert "Playwright" in title
        await browser.close()