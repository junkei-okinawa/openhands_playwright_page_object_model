import allure
import pytest
from playwright.async_api import Page

from pages.home_page import HomePage
from pages.posts_page import PostsPage


@pytest.mark.asyncio
@allure.epic("Posts Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("This test verifies that the Posts page title is correct.")
@allure.id("16")
@pytest.mark.posts
async def test_posts_page_title(home_page: HomePage):
    with allure.step("Navigate to the Hugging Face home page"):
        await home_page.goto("https://huggingface.co/")
    with allure.step("Click the Posts page"):
        posts_page = await home_page.click_posts_tab()
    with allure.step("Verify the title of the Posts page"):
        assert "Hugging Face – Posts" == await posts_page.page.title()
