import allure
import pytest
from playwright.async_api import Page

from pages.posts_page import PostsPage


@pytest.mark.asyncio
@allure.epic("Posts Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("This test verifies that the Posts page title is correct.")
@allure.id("16")
@pytest.mark.posts
async def test_posts_page_title(page: Page, base_url):
    with allure.step("Navigate to the Posts page"):
        posts_page = PostsPage(page)
        await posts_page.navigate()
    with allure.step("Verify the title of the Posts page"):
        assert "Blog" in await posts_page.get_page_title()
