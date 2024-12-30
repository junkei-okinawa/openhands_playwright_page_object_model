import pytest
import asyncio
from playwright.async_api import async_playwright
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
        print("Navigated to Models page successfully")
        await page.screenshot(path="tests/screenshots/models_page.png")
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
        first_model_title = await models_page.get_first_model_card_title_text()
        assert first_model_title.lower() != ""
        print(f"First model card title: {first_model_title}")
        await page.screenshot(path="tests/screenshots/search_results.png")
        await browser.close()

async def main():
    await test_navigate_to_models_page()
    await test_search_models()

if __name__ == '__main__':
    asyncio.run(main())