import pytest
from playwright.sync_api import Page

from pages.posts_page import PostsPage


import pytest
from playwright.sync_api import Page

from pages.posts_page import PostsPage
import allure

@pytest.mark.asyncio
@allure.epic("Posts Page Tests")
@allure.feature("Navigation")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("This test verifies that the Posts page title is correct.")
@allure.id("12")
@pytest.mark.posts
async def test_posts_page_title(page: Page, base_url):
    posts_page = PostsPage(page)
    await posts_page.navigate()
    assert "Blog" in await posts_page.get_page_title()
