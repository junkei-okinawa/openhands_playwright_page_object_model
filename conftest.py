import os
import sys
import asyncio
from typing import Dict
from pathlib import Path

import allure
import pytest
from playwright.async_api import async_playwright, Browser, BrowserContext, Page

sys.path.insert(0, str(Path(__file__).parent))

@pytest.fixture(scope="function")
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
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


def pytest_runtest_makereport(item, call):
    if "page" in item.fixturenames:  # page フィクスチャを使用しているテストのみ処理
        if call.when == "call":
            # teardown時にテストの失敗を判定できるようにitem(node)にexcinfoを格納
            item.excinfo = call.excinfo
        elif call.when == "teardown":
            if item.excinfo:
                # テストが失敗した場合の処理
                if hasattr(item, '_context_video_path') and item._context_video_path:
                    print(f"レポートに動画を添付します")
                    try:
                        allure.attach.file(
                            item._context_video_path,
                            name=f"{item.name}-video-on-failure",
                            attachment_type=allure.attachment_type.WEBM
                        )
                        print(f"動画の添付に成功しました")
                    except Exception as e:
                        print(f"動画添付中にエラー: {e}")
