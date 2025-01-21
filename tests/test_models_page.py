import allure
import pytest
import asyncio
from playwright.async_api import Page, expect

from pages.home_page import HomePage


@pytest.mark.asyncio
@allure.epic("Models Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("This test verifies that navigating to the Models page displays the correct title.")
@allure.id("10")
async def test_navigate_to_models_page(home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    with allure.step("Navigate to the Models page"):
        models_page = await home_page.navigate_to_models_page()
    with allure.step("Verify the title of the Models page"):
        title_text = await models_page.get_title_text()
        assert title_text == "Models"


@pytest.mark.asyncio
@allure.epic("Models Page Tests")
@allure.feature("Search")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("This test verifies that searching for models displays the correct filter.")
@allure.id("11")
async def test_search_models(home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    with allure.step("Navigate to the Models page"):

        models_page = await home_page.navigate_to_models_page()
    with allure.step("Search for models"):
        await models_page.search_models("bert")
    with allure.step("Verify the search filter"):
        await expect(models_page.filter_by_name_box).to_have_value("bert")