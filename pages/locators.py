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
        """xpath=//a[@href='https://ui.endpoints.huggingface.co']"""
    )
    MENU_BUTTON = """xpath=//div[@class="relative group"]/button"""


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


class InferenceEndpointsPageLocators:
    TITLE = """xpath=//h1"""
    TITLE_H2 = """xpath=//h2"""


class TasksPageLocators:
    TITLE = """xpath=//h1"""
