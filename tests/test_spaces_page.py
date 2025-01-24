import asyncio

import allure
import pytest

from pages.home_page import HomePage
from pages.spaces_page import SpacesPage


@pytest.mark.asyncio
@allure.epic("Spaces Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("This test verifies that the Spaces page title is correct.")
@allure.id("16")
async def test_spaces_page_title(home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    with allure.step("Click the Spaces tab"):
        spaces_page = await home_page.click_spaces_tab()
    with allure.step("Verify the title of the Spaces page"):
        assert "Spaces - Hugging Face" == await spaces_page.page.title()