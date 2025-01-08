from cssselect import GenericTranslator
import re

def convert_css_to_xpath(css_selector):
    translator = GenericTranslator()
    try:
        return translator.css_to_xpath(css_selector)
    except Exception as e:
        if "Expected selector, got <DELIM '/' at 0>" in str(e):
            return f"xpath=//{css_selector}"
        else:
            if css_selector.startswith('input[placeholder="'):
                return f"xpath=//input[@placeholder='{css_selector.split('input[placeholder="')[1].split(']')[0]}']"
            elif css_selector.startswith('nav a[href="'):
                return f"descendant-or-self::nav/descendant-or-self::*/a[@href = '{css_selector.split('nav a[href="')[1].split('"]')[0]}']".replace("xpath=///", "")
            else:
                return f"xpath=//{css_selector}"

def process_locators_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    def replace_locator(match):
        locator_string = match.group(1)
        if not locator_string.startswith('xpath='):
            xpath_locator = convert_css_to_xpath(locator_string)
            return f"= '{xpath_locator}'"
        else:
            return match.group(0)

    pattern = r"=\s*'([^']+)'"
    modified_content = re.sub(pattern, replace_locator, content)

    with open(file_path, 'w') as f:
        f.write(modified_content)

if __name__ == "__main__":
    process_locators_file('pages/locators.py')