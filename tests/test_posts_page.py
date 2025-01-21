import pytest
from playwright.sync_api import Page

from pages.posts_page import PostsPage


@pytest.mark.asyncio
@pytest.mark.posts
async def test_posts_page_title(page: Page, base_url):
    posts_page = PostsPage(page)
    await posts_page.navigate()
    assert "Blog" in await posts_page.get_page_title()
