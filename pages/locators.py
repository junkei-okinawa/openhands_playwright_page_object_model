class HomePageLocators:
    MODELS_TAB = """xpath=//nav//a[@href="/models"]"""
    DATASETS_TAB = """xpath=//nav//a[@href="/datasets"]"""
    SPACES_TAB = """xpath=//nav//a[@href="/spaces"]"""
    POSTS_TAB = """xpath=//nav//a[@href="/posts"]"""
    DOCS_TAB = """xpath=//nav//a[@href="/docs"]"""
    ENTERPRISE_TAB = """xpath=//nav//a[@href="/enterprise"]"""
    PRICING_TAB = """xpath=//nav//a[@href="/pricing"]"""
    TASKS_LINK = """xpath=//a[@href="/tasks"]"""
    INFERENCE_ENDPOINTS_LINK = (
        """xpath=//a[contains(@href,'endpoints.huggingface.co')]"""
    )
    HUGGINGCHAT_LINK = (
        """xpath=//a[contains(@href,'/chat') and contains(@class,'rounded-lg')]"""
    )
    MENU_BUTTON = """xpath=//div[@class="relative group"]/button"""
    ABOUT_LINK_FOOTER = """xpath=//footer//a[@href="/huggingface"]"""
    BRAND_ASSETS_LINK_FOOTER = """xpath=//footer//a[@href="/brand"]"""
    TERMS_OF_SERVICE_LINK_FOOTER = """xpath=//footer//a[@href="/terms-of-service"]"""
    PRIVACY_LINK_FOOTER = """xpath=//footer//a[@href="/privacy"]"""
    JOBS_LINK_FOOTER = """xpath=//footer//a[contains(@href, 'workable.com')]"""


class ModelsPageLocators:
    TITLE = """xpath=//h1"""
    SEARCH_BOX = """xpath=//input[starts-with(@placeholder, "Search models")]"""
    SEE_ALL_MODEL_RESULTS_FOR_ELEMENT = (
        """xpath=//li/a/span[contains(text(),"model results for")]"""
    )
    FILTER_BY_NAME_BOX = """xpath=//input[@placeholder="Filter by name"]"""
    FIRST_MODEL_CARD_TITLE = """xpath=//article[1]/h4"""


class DatasetsPageLocators:
    TITLE = """xpath=//h1"""
    BROWSE_DATASETS_BUTTON = (
        """xpath=//article[contains(@class, "overview-card-wrapper")][1]"""
    )


class SpacesPageLocators:
    TITLE = """xpath=//h1"""


class PostsPageLocators:
    TITLE = """xpath=//h1"""


class DocsPageLocators:
    TITLE = """xpath=//h1"""


class EnterprisePageLocators:
    TITLE = """xpath=//h1"""


class PricingPageLocators:
    TITLE = """xpath=//h1"""


class TasksPageLocators:
    TITLE = """xpath=//h1"""


class HuggingChatPageLocators:
    TITLE = """xpath=//h2[contains(text(), 'HuggingChat')]"""
    CHAT_INPUT = """xpath=//textarea[contains(@placeholder, 'Ask')]"""
    NEW_CHAT_BUTTON = (
        """xpath=//a[contains(@href, '/chat') and normalize-space(text())='New Chat']"""
    )


class InferenceEndpointsPageLocators:
    TITLE = """xpath=//h1"""
    TITLE_H2 = """xpath=//h2"""
    # 料金プランセクション
    PRICING_PLANS = """xpath=//div[contains(@class, 'pricing-table')]"""
    PRICING_PLAN_CARDS = """xpath=//div[contains(@class, 'pricing-card')]"""
    # デプロイセクション
    DEPLOY_BUTTON = (
        """xpath=//a[contains(@href, '/deploy') or contains(text(), 'Deploy')]"""
    )
    GET_STARTED_BUTTON = """xpath=//a[contains(text(), 'Get Started')]"""
    # 機能説明セクション
    FEATURES_SECTION = """xpath=//section[contains(@class, 'features-section')]"""
    FEATURES_CARDS = """xpath=//div[contains(@class, 'feature-card')]"""


class AboutPageLocators:
    TITLE = """xpath=//h1"""


class BrandAssetsPageLocators:
    TITLE = """xpath=//h2"""


class TermsOfServicePageLocators:
    TITLE = """xpath=//h1[contains(text(), 'Terms of Service')]"""


class PrivacyPageLocators:
    TITLE = """xpath=//h1[contains(text(), 'Privacy')]"""
