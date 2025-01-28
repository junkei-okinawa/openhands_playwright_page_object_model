from playwright.async_api import Page

from .about_page import AboutPage
from .base_page import BasePage
from .brand_assets_page import BrandAssetsPage
from .datasets_page import DatasetsPage
from .docs_page import DocsPage
from .enterprise_page import EnterprisePage
from .huggingchat_page import HuggingChatPage
from .inference_endpoints_page import InferenceEndpointsPage
from .locators import HomePageLocators
from .models_page import ModelsPage
from .posts_page import PostsPage
from .pricing_page import PricingPage
from .privacy_page import PrivacyPage
from .spaces_page import SpacesPage
from .tasks_page import TasksPage
from .terms_of_service_page import TermsOfServicePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.locators = HomePageLocators

    @property
    def models_tab(self):
        return self.page.locator(self.locators.MODELS_TAB)

    async def click_models_tab(self):
        await self.models_tab.click()
        await self.page.wait_for_load_state()
        return ModelsPage(self.page)

    @property
    def datasets_tab(self):
        return self.page.locator(self.locators.DATASETS_TAB)

    async def click_datasets_tab(self):
        await self.datasets_tab.click()
        await self.page.wait_for_load_state()
        return DatasetsPage(self.page)

    @property
    def spaces_tab(self):
        return self.page.locator(self.locators.SPACES_TAB)

    async def click_spaces_tab(self):
        await self.spaces_tab.click()
        await self.page.wait_for_load_state()
        return SpacesPage(self.page)

    @property
    def posts_tab(self):
        return self.page.locator(self.locators.POSTS_TAB)

    async def click_posts_tab(self):
        await self.posts_tab.click()
        await self.page.wait_for_load_state()
        return PostsPage(self.page)

    @property
    def docs_tab(self):
        return self.page.locator(self.locators.DOCS_TAB)

    async def click_docs_tab(self):
        await self.docs_tab.click()
        await self.page.wait_for_load_state()
        return DocsPage(self.page)

    @property
    def enterprise_tab(self):
        return self.page.locator(self.locators.ENTERPRISE_TAB)

    async def click_enterprise_tab(self):
        await self.enterprise_tab.click()
        await self.page.wait_for_load_state()
        return EnterprisePage(self.page)

    @property
    def pricing_tab(self):
        return self.page.locator(self.locators.PRICING_TAB)

    async def click_pricing_tab(self):
        await self.pricing_tab.click()
        await self.page.wait_for_load_state()
        return PricingPage(self.page)

    @property
    def tasks_link(self):
        return self.page.locator(self.locators.TASKS_LINK)

    async def click_tasks_link(self):
        await self.tasks_link.click()
        await self.page.wait_for_load_state()
        return TasksPage(self.page)

    @property
    def inference_endpoints_link(self):
        return self.page.locator(self.locators.INFERENCE_ENDPOINTS_LINK)

    async def click_inference_endpoints_link(self):
        async with self.page.expect_popup() as new_page_info:
            await self.inference_endpoints_link.click()
        new_page = await new_page_info.value
        return InferenceEndpointsPage(new_page)

    @property
    def huggingchat_link(self):
        return self.page.locator(self.locators.HUGGINGCHAT_LINK)

    async def click_huggingchat_link(self):
        await self.huggingchat_link.click()
        await self.page.wait_for_load_state("networkidle")
        return HuggingChatPage(self.page)

    @property
    def about_link_footer(self):
        return self.page.locator(self.locators.ABOUT_LINK_FOOTER)

    async def click_about_link_footer(self):
        await self.about_link_footer.click()
        await self.page.wait_for_load_state()
        return AboutPage(self.page)

    @property
    def brand_assets_link_footer(self):
        return self.page.locator(self.locators.BRAND_ASSETS_LINK_FOOTER)

    async def click_brand_assets_link_footer(self):
        await self.brand_assets_link_footer.click()
        await self.page.wait_for_load_state()
        return BrandAssetsPage(self.page)

    @property
    def terms_of_service_link_footer(self):
        return self.page.locator(self.locators.TERMS_OF_SERVICE_LINK_FOOTER)

    async def click_terms_of_service_link_footer(self):
        await self.terms_of_service_link_footer.click()
        await self.page.wait_for_load_state()
        return TermsOfServicePage(self.page)

    @property
    def privacy_link_footer(self):
        return self.page.locator(self.locators.PRIVACY_LINK_FOOTER)

    async def click_privacy_link_footer(self):
        await self.privacy_link_footer.click()
        await self.page.wait_for_load_state()
        return PrivacyPage(self.page)

    @property
    def jobs_link_footer(self):
        return self.page.locator(self.locators.JOBS_LINK_FOOTER)

    async def click_jobs_link_footer(self):
        await self.jobs_link_footer.click()
        return self.page
