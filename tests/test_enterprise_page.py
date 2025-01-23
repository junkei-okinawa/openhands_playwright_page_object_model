import allure
import pytest
from playwright.async_api import Page

from pages.home_page import HomePage
from pages.enterprise_page import EnterprisePage


@pytest.mark.asyncio
@allure.epic("Enterprise Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("This test verifies that the Enterprise page title is correct.")
@allure.id("17")
@pytest.mark.enterprise
async def test_enterprise_page_title(home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    with allure.step("Click the the Enterprise link"):
        enterprise_page = await home_page.click_enterprise_tab()
    with allure.step("Verify the title of the Enterprise page"):
        assert "Enterprise Hub - Hugging Face" in await enterprise_page.page.title()

