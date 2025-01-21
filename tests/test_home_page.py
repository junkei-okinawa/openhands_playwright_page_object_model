import asyncio

import allure
import pytest
from playwright.async_api import Page

from pages.home_page import HomePage
from pages.spaces_page import SpacesPage


@pytest.mark.asyncio
@allure.epic("Home Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test clicking the Models tab")
@allure.description(
    "This test verifies that clicking the Models tab navigates to the correct page and displays the expected title."
)
@allure.id("1")
async def test_click_models_tab(home_page: HomePage, test_data):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    tab_data = next(
        tab for tab in test_data["home_page_tabs"] if tab["tab_name"] == "models"
    )
    with allure.step("Click the Models tab"):
        models_page = await home_page.click_models_tab()
    with allure.step("Verify the title of the Models page"):
        title_text = await models_page.get_title_text()
        assert title_text == tab_data["expected_title"]


@pytest.mark.asyncio
@allure.epic("Home Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test clicking the Datasets tab")
@allure.description(
    "This test verifies that clicking the Datasets tab navigates to the correct page and displays the expected title."
)
@allure.id("2")
async def test_click_datasets_tab(home_page: HomePage, test_data):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    tab_data = next(
        tab for tab in test_data["home_page_tabs"] if tab["tab_name"] == "datasets"
    )
    with allure.step("Click the Datasets tab"):
        datasets_page = await home_page.click_datasets_tab()
    with allure.step("Verify the title of the Datasets page"):
        title_text = await datasets_page.get_title_text()
        assert title_text == tab_data["expected_title"]


@pytest.mark.asyncio
@allure.epic("Home Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test clicking the Spaces tab")
@allure.description(
    "This test verifies that clicking the Spaces tab navigates to the correct page and displays the expected title."
)
@allure.id("3")
async def test_click_spaces_tab(home_page: HomePage, test_data):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    tab_data = next(
        tab for tab in test_data["home_page_tabs"] if tab["tab_name"] == "spaces"
    )
    with allure.step("Click the Spaces tab"):
        spaces_page = await home_page.click_spaces_tab()
    with allure.step("Verify the title of the Spaces page"):
        title_text = await spaces_page.get_page_title()
        assert "Spaces" in title_text


@pytest.mark.asyncio
@allure.epic("Home Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test clicking the Posts tab")
@allure.description(
    "This test verifies that clicking the Posts tab navigates to the correct page."
)
@allure.id("4")
async def test_click_posts_tab(home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    with allure.step("Click the Posts tab"):
        posts_page = await home_page.click_posts_tab()
        assert "Posts" in await posts_page.get_page_title()


@pytest.mark.asyncio
@allure.epic("Home Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test clicking the Docs tab")
@allure.description(
    "This test verifies that clicking the Docs tab navigates to the correct page."
)
@allure.id("5")
async def test_click_docs_tab(home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    with allure.step("Click the Docs tab"):
        docs_page = await home_page.click_docs_tab()
        assert "Documentation" in await docs_page.get_page_title()


@pytest.mark.asyncio
@allure.epic("Home Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test clicking the Enterprise tab")
@allure.description(
    "This test verifies that clicking the Enterprise tab navigates to the correct page."
)
@allure.id("6")
async def test_click_enterprise_tab(home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    with allure.step("Click the Enterprise tab"):
        enterprise_page = await home_page.click_enterprise_tab()
        assert "Enterprise" in await enterprise_page.get_page_title()


@pytest.mark.asyncio
@allure.epic("Home Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test clicking the Pricing tab")
@allure.description(
    "This test verifies that clicking the Pricing tab navigates to the correct page."
)
@allure.id("7")
async def test_click_pricing_tab(home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    with allure.step("Click the Pricing tab"):
        pricing_page = await home_page.click_pricing_tab()
        assert "Pricing" in await pricing_page.get_page_title()


@pytest.mark.asyncio
@allure.epic("Home Page Tests")
@allure.feature("Failure Handling")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test that is intentionally failing")
@allure.description(
    "This test is intentionally failing to demonstrate the Allure report's failure handling."
)
@allure.id("8")
async def test_failing_test(page: Page):
    with allure.step("Verify the page title"):
        assert await page.title() == "Wrong Title"
