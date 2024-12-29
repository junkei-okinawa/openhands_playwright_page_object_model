from playwright.async_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.models_tab = page.locator('nav a[href="/models"]')

    async def click_models_tab(self):
        await self.models_tab.click()

    @property
    def datasets_tab(self):
        return self.page.locator('nav a[href="/datasets"]')

    async def click_datasets_tab(self):
        await self.datasets_tab.click()

    @property
    def spaces_tab(self):
        return self.page.locator('nav a[href="/spaces"]')

    async def click_spaces_tab(self):
        await self.spaces_tab.click()

    @property
    def posts_tab(self):
        return self.page.locator('nav a[href="/posts"]')

    async def click_posts_tab(self):
        await self.posts_tab.click()

    @property
    def docs_tab(self):
        return self.page.locator('nav a[href="/docs"]')

    async def click_docs_tab(self):
        await self.docs_tab.click()

    @property
    def enterprise_tab(self):
        return self.page.locator('nav a[href="/enterprise"]')

    async def click_enterprise_tab(self):
        await self.enterprise_tab.click()

    @property
    def pricing_tab(self):
        return self.page.locator('nav a[href="/pricing"]')

    async def click_pricing_tab(self):
        await self.pricing_tab.click()