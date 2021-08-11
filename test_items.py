from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_exist(browser):
    browser.get(link)
    assert WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary'))
    ), "element isn't found"
