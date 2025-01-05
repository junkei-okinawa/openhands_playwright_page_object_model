import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pytest
from playwright.async_api import async_playwright
import allure
import asyncio
from pathlib import Path

@pytest.fixture(scope="function")
async def video_recording(request):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        test_name = request.node.name
        context = await browser.new_context(record_video="on", record_video_dir=f"{Path(__file__).parent}/videos")
        page = await context.new_page()
        yield page
        if request.node.rep_call.failed:
            try:
                video_path = await page.video.path()
                with open(video_path, "rb") as video_file:
                    allure.attach(video_file.read(), name="video", attachment_type=allure.attachment_type.WEBM)
            except FileNotFoundError:
                pass
        await page.close()
        await context.close()
        await browser.close()

def pytest_runtest_makereport(item, call):
    if call.when == "call":
        item.rep_call = call