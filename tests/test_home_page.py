import allure
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
        png_bytes = await page.screenshot()
        allure.attach(png_bytes, name="models_tab", attachment_type=allure.attachment_type.PNG)
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
        png_bytes = await page.screenshot()
        allure.attach(png_bytes, name="datasets_tab", attachment_type=allure.attachment_type.PNG)
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
        png_bytes = await page.screenshot()
        allure.attach(png_bytes, name="spaces_tab", attachment_type=allure.attachment_type.PNG)
        await browser.close()

@pytest.mark.asyncio
async def test_click_posts_tab():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://huggingface.co/")
        home_page = HomePage(page)
        await home_page.click_posts_tab()
        png_bytes = await page.screenshot()
        allure.attach(png_bytes, name="posts_tab", attachment_type=allure.attachment_type.PNG)
        await browser.close()

@pytest.mark.asyncio
async def test_click_docs_tab():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://huggingface.co/")
        home_page = HomePage(page)
        await home_page.click_docs_tab()
        png_bytes = await page.screenshot()
        allure.attach(png_bytes, name="docs_tab", attachment_type=allure.attachment_type.PNG)
        await browser.close()

@pytest.mark.asyncio
async def test_click_enterprise_tab():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://huggingface.co/")
        home_page = HomePage(page)
        await home_page.click_enterprise_tab()
        png_bytes = await page.screenshot()
        allure.attach(png_bytes, name="enterprise_tab", attachment_type=allure.attachment_type.PNG)
        await browser.close()

@pytest.mark.asyncio
async def test_click_pricing_tab():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://huggingface.co/")
        home_page = HomePage(page)
        await home_page.click_pricing_tab()
        png_bytes = await page.screenshot()
        allure.attach(png_bytes, name="pricing_tab", attachment_type=allure.attachment_type.PNG)
        await browser.close()
