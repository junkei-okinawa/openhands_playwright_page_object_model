import allure
import pytest
from playwright.async_api import Page

from pages.home_page import HomePage
from pages.inference_endpoints_page import InferenceEndpointsPage


@pytest.mark.asyncio
@allure.epic("Inference Endpoints Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test clicking the Inference Endpoints link")
@allure.description(
    "This test verifies that clicking the Inference Endpoints link navigates to the correct page and displays the expected title."
)
@allure.id("20")
async def test_inference_endpoints_page_title(page: Page, home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    with allure.step("Click the Inference Endpoints link and wait for new page"):
        inference_endpoints_page = await home_page.click_inference_endpoints_link()
    with allure.step("Verify the title of the Inference Endpoints page"):
        await inference_endpoints_page.wait_for_load_state()
        assert "Inference Endpoints by Hugging Face" == await inference_endpoints_page.page.title()
