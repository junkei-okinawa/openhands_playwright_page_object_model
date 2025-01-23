import asyncio

import allure
import pytest
from playwright.async_api import expect

from pages.home_page import HomePage
from pages.models_page import ModelsPage


@pytest.mark.asyncio
@allure.epic("Models Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    "This test verifies that navigating to the Models page displays the correct title."
)
@allure.id("10")
async def test_models_page_title(home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    with allure.step("Navigate to the Models page"):
        models_page = await home_page.click_models_tab()
    with allure.step("Verify the title of the Models page"):
        assert "Models - Hugging Face" == await models_page.page.title()


@pytest.mark.asyncio
@allure.epic("Models Page Tests")
@allure.feature("Search")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    "This test verifies that searching for models displays the correct filter."
)
@allure.id("11")
async def test_search_models(home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    with allure.step("Navigate to the Models page"):
        models_page = await home_page.click_models_tab()
    with allure.step("Search for models"):
        await models_page.search_models("bert")
    with allure.step("Verify the search filter"):
        assert await models_page.filter_by_name_box.input_value() == "bert"
