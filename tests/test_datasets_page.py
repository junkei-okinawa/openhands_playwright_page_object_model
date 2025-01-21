import asyncio

import allure
import pytest

from pages.datasets_page import DatasetsPage
from pages.home_page import HomePage


@pytest.mark.asyncio
@allure.epic("Datasets Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("This test verifies that the Datasets page title is correct.")
@allure.id("9")
async def test_datasets_page_title(home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    with allure.step("Click the Datasets tab"):
        datasets_page = await home_page.click_datasets_tab()
    with allure.step("Verify the title of the Datasets page"):
        title_text = await datasets_page.get_title_text()
        assert title_text == "Datasets"
