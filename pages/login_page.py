from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.std_user_inventory_page import StdUserInvPage

USER_NAME_LOCATOR = (By.ID, "user-name")
PWD_LOCATOR = (By.ID, "password")
LOGIN_BUTTON_LOCATOR = (By.NAME, "login-button")
ERROR_CONTAINER_LOCATOR = (By.CLASS_NAME, 'error-message-container')
ERROR_CROSS_BUTTON = (By.CLASS_NAME, 'error-button')
LOGIN_BUTTON_FRAME_LOCATOR = (By.ID, 'login_button_container')


class LoginPage(BasePage):
    def __init__(self, driver, url=' '):
        super().__init__(driver, url)

    def get_user_form(self):
        return self.driver.find_element(*USER_NAME_LOCATOR)

    def fill_in_user(self, user):
        self.get_user_form().send_keys(user)

    def get_pwd_form(self):
        return self.driver.find_element(*PWD_LOCATOR)

    def fill_in_pwd(self, password):
        self.get_pwd_form().send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LOGIN_BUTTON_LOCATOR).click()

    def log_in_user(self, user, pwd):
        self.fill_in_user(user)
        self.fill_in_pwd(pwd)
        self.click_login_button()
        if user != 'locked_out_user':
            return StdUserInvPage(self.driver, self.driver.current_url)

    def find_error_frame(self):
        return self.driver.find_element(*ERROR_CONTAINER_LOCATOR)

    def get_error_message(self):
        return self.find_error_frame().get_attribute('innerText')

    def click_error_cross_button(self):
        self.driver.find_element(*ERROR_CROSS_BUTTON).click()

    def wait_for_error_frame_to_disappear(self):
        return WebDriverWait(self.driver, 2).until_not(EC.presence_of_element_located(self.get_error_message()))

    def wait_for_delay_user_to_log_on(self):
        return WebDriverWait(self.driver, 7).until_not(EC.presence_of_element_located(LOGIN_BUTTON_LOCATOR))










