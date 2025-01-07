class HomePageLocators:
    MODELS_TAB = 'nav a[href="/models"]'
    DATASETS_TAB = 'nav a[href="/datasets"]'
    SPACES_TAB = 'nav a[href="/spaces"]'
    POSTS_TAB = 'nav a[href="/posts"]'
    DOCS_TAB = 'nav a[href="/docs"]'
    ENTERPRISE_TAB = 'nav a[href="/enterprise"]'
    PRICING_TAB = 'nav a[href="/pricing"]'

class ModelsPageLocators:
    TITLE = 'h1'
    SEARCH_BOX = 'input[placeholder^="Search models"]'
    SEE_ALL_MODEL_RESULTS_FOR_ELEMENT = 'xpath=//li/a/span[contains(text(),"model results for")]'
    FILTER_BY_NAME_BOX = 'input[placeholder="Filter by name"]'
    FIRST_MODEL_CARD_TITLE = 'article:first-child h4'

class DatasetsPageLocators:
    TITLE = 'h1'
    BROWSE_DATASETS_BUTTON = 'xpath=//article[contains(@class, "overview-card-wrapper")][1]'

class SpacesPageLocators:
    TITLE = 'h1'