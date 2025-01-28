import allure
import pytest
from playwright.async_api import Page

from pages.home_page import HomePage


@pytest.mark.asyncio
@allure.epic("Inference Endpoints Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test navigation to Inference Endpoints page")
@allure.description(
    """
    This test verifies:
    1. Inference Endpoints link exists on the home page
    2. Link opens in a new tab
    3. New tab has the correct URL and title
    """
)
@allure.id("20")
async def test_inference_endpoints_navigation(page: Page, home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")

    with allure.step("Verify Inference Endpoints link exists"):
        link = page.locator('xpath=//a[contains(@href,"endpoints.huggingface.co")]')
        await link.wait_for(state="visible")
        assert await link.is_visible()

    with allure.step("Click Inference Endpoints link and wait for new tab"):
        inference_endpoints_page = await home_page.click_inference_endpoints_link()

    with allure.step("Verify new tab URL and title"):
        await inference_endpoints_page.wait_for_page_load()
        # URLのドメイン部分を検証
        assert "endpoints.huggingface.co" in inference_endpoints_page.page.url
        title = await inference_endpoints_page.get_page_title()
        assert "Inference Endpoints" in title


@pytest.mark.asyncio
@allure.epic("Inference Endpoints Page Tests")
@allure.feature("Pricing Plans")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test pricing plans display")
@allure.description(
    """
    This test verifies:
    1. Pricing plans section is visible
    2. Multiple pricing plan cards are displayed
    """
)
@allure.id("21")
async def test_pricing_plans_display(home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")

    with allure.step("Navigate to Inference Endpoints page"):
        inference_endpoints_page = await home_page.click_inference_endpoints_link()
        await inference_endpoints_page.wait_for_page_load()

    with allure.step("Verify pricing plans section is visible"):
        assert await inference_endpoints_page.verify_pricing_plans_visible()

    with allure.step("Verify multiple pricing plan cards exist"):
        plan_count = await inference_endpoints_page.get_pricing_plan_count()
        assert plan_count > 0, "No pricing plan cards found"


@pytest.mark.asyncio
@allure.epic("Inference Endpoints Page Tests")
@allure.feature("Deploy Button")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test deploy button visibility")
@allure.description(
    """
    This test verifies:
    1. Deploy button is visible on the page
    """
)
@allure.id("22")
async def test_deploy_button_visibility(home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")

    with allure.step("Navigate to Inference Endpoints page"):
        inference_endpoints_page = await home_page.click_inference_endpoints_link()
        await inference_endpoints_page.wait_for_page_load()

    with allure.step("Verify deploy button is visible"):
        assert await inference_endpoints_page.verify_deploy_button_visible()


@pytest.mark.asyncio
@allure.epic("Inference Endpoints Page Tests")
@allure.feature("Features Section")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test features section display")
@allure.description(
    """
    This test verifies:
    1. Features section is visible
    2. Multiple feature cards are displayed
    """
)
@allure.id("23")
async def test_features_section_display(home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")

    with allure.step("Navigate to Inference Endpoints page"):
        inference_endpoints_page = await home_page.click_inference_endpoints_link()
        await inference_endpoints_page.wait_for_page_load()

    with allure.step("Verify features section is visible"):
        assert await inference_endpoints_page.verify_features_visible()

    with allure.step("Verify multiple feature cards exist"):
        features_count = await inference_endpoints_page.get_features_count()
        assert features_count > 0, "No feature cards found"
