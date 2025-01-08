import sys
import json
from pathlib import Path

import allure
import pytest
from playwright.async_api import async_playwright, Browser, BrowserContext, Page

from pages.home_page import HomePage


sys.path.insert(0, str(Path(__file__).parent))


@pytest.fixture(scope="function")
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        yield browser
        await browser.close()


@pytest.fixture
async def context(request, browser: Browser, tmpdir_factory: pytest.TempdirFactory):
    context = await browser.new_context(record_video_dir=tmpdir_factory.mktemp('videos'))
    yield context
    await context.close()


@pytest.fixture
async def page(request, context: BrowserContext, base_url: str):
    page: Page = await context.new_page()
    await page.goto(base_url)
    yield page
    png_bytes = await page.screenshot()  # context.pages[0] ではなく page から取得
    allure.attach(png_bytes, name=request.node.name, attachment_type=allure.attachment_type.PNG)
    video_path = await page.video.path()
    request.node._context_video_path = video_path  # 後でフック関数からアクセスできるように保存
    await page.close()


@pytest.fixture
async def home_page(page: Page):
    return HomePage(page)


@pytest.fixture
def test_data():
    with open("tests/test_data.json", "r") as f:
        return json.load(f)


def pytest_runtest_makereport(item, call):
    if "page" in item.fixturenames:  # page フィクスチャを使用しているテストのみ処理
        if call.when == "call":
            print("""call.when == "call" """)
            # teardown時にテストの失敗を判定できるようにitem(node)にexcinfoを格納
            item.excinfo = call.excinfo
        elif call.when == "teardown":
            print("""call.when == "teardown" """)
            print(f"hasattr(item, '_context_video_path'): {hasattr(item, '_context_video_path')}")
            print(F"item._context_video_path: {item._context_video_path}")
            print(f"item.excinfo: {item.excinfo}")
            if item.excinfo:
                # テストが失敗した場合の処理
                if hasattr(item, '_context_video_path') and item._context_video_path:
                    try:
                        allure.attach.file(
                            item._context_video_path,
                            name=f"{item.name}-video-on-failure",
                            attachment_type=allure.attachment_type.WEBM
                        )
                    except Exception as e:
                        allure.attach(f"Error while attaching video: {e}")
