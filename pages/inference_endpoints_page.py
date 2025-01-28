from playwright.async_api import Page, expect

from pages.base_page import BasePage
from pages.locators import InferenceEndpointsPageLocators


class InferenceEndpointsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = InferenceEndpointsPageLocators()

    async def wait_for_page_load(self):
        """
        Wait for the Inference Endpoints page to load in new tab
        """
        await self.wait_for_load_state()
        # 新しいタブでページが読み込まれるのを待つ
        await self.page.wait_for_load_state("domcontentloaded")

    async def get_page_title(self) -> str:
        """
        Get the page title of the Inference Endpoints page.
        Returns:
            str: The page title
        """
        await self.wait_for_page_load()
        return await self.page.title()

    @property
    def pricing_plans(self):
        """料金プランセクションを取得"""
        return self.page.locator(self.locators.PRICING_PLANS)

    @property
    def pricing_plan_cards(self):
        """料金プランカードを取得"""
        return self.page.locator(self.locators.PRICING_PLAN_CARDS)

    @property
    def deploy_button(self):
        """デプロイボタンを取得"""
        return self.page.locator(self.locators.DEPLOY_BUTTON)

    @property
    def get_started_button(self):
        """Get Startedボタンを取得"""
        return self.page.locator(self.locators.GET_STARTED_BUTTON)

    @property
    def features_section(self):
        """機能説明セクションを取得"""
        return self.page.locator(self.locators.FEATURES_SECTION)

    @property
    def features_cards(self):
        """機能説明カードを取得"""
        return self.page.locator(self.locators.FEATURES_CARDS)

    async def verify_pricing_plans_visible(self) -> bool:
        """
        料金プランセクションが表示されているか確認
        Returns:
            bool: 表示されている場合True
        """
        await self.pricing_plans.wait_for(state="visible")
        return await self.pricing_plans.is_visible()

    async def get_pricing_plan_count(self) -> int:
        """
        料金プランの数を取得
        Returns:
            int: 料金プランの数
        """
        return await self.pricing_plan_cards.count()

    async def verify_deploy_button_visible(self) -> bool:
        """
        デプロイボタンが表示されているか確認
        Returns:
            bool: 表示されている場合True
        """
        await self.deploy_button.wait_for(state="visible")
        return await self.deploy_button.is_visible()

    async def verify_features_visible(self) -> bool:
        """
        機能説明セクションが表示されているか確認
        Returns:
            bool: 表示されている場合True
        """
        await self.features_section.wait_for(state="visible")
        return await self.features_section.is_visible()

    async def get_features_count(self) -> int:
        """
        機能説明カードの数を取得
        Returns:
            int: 機能説明カードの数
        """
        return await self.features_cards.count()
