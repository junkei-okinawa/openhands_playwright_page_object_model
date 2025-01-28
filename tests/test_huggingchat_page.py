import pytest
from playwright.async_api import Page

from pages.home_page import HomePage


@pytest.mark.asyncio
async def test_navigate_to_huggingchat_page(page: Page, base_url: str) -> None:
    """HuggingChatページへの遷移をテストする"""
    # Arrange
    home_page = HomePage(page)
    await page.goto(base_url)

    # ページの完全な読み込みを待機
    await page.wait_for_load_state("networkidle")

    # New Chatリンクが表示されるまで待機
    chat_link = page.locator(home_page.locators.HUGGINGCHAT_LINK)
    await chat_link.wait_for(state="visible", timeout=10000)

    # Act
    huggingchat_page = await home_page.click_huggingchat_link()

    # ページの完全な読み込みを待機
    await huggingchat_page.page.wait_for_load_state("networkidle")

    # Assert
    current_url = page.url
    assert "/chat" in current_url, f"Expected URL to contain '/chat', but got {current_url}"

    # ロゴが表示されることを確認
    title = huggingchat_page.page.locator(huggingchat_page.locators.TITLE)
    assert await title.is_visible(), "HuggingChat logo should be visible"

    # チャット入力とNew Chatボタンが表示されることを確認
    try:
        assert await huggingchat_page.is_chat_input_visible(), "Chat input should be visible"
        assert await huggingchat_page.is_new_chat_button_visible(), "New chat button should be visible"
    except Exception as e:
        page_content = await page.content()
        print(f"Page content: {page_content[:500]}...")  # 最初の500文字だけ表示
        raise AssertionError(f"Failed to verify chat input: {str(e)}")
