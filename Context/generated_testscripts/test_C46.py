import pytest
import subprocess
import platform
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Page Object Classes
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    def verify_element_visible(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        assert element.is_displayed(), f"Element {locator} is not visible"
        return element
    def verify_element_enabled(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        assert element.is_enabled(), f"Element {locator} is not enabled"
        return element
    def click_element(self, locator):
        element = self.verify_element_enabled(locator)
        element.click()
    def get_text(self, locator):
        element = self.verify_element_visible(locator)
        return element.text
    def verify_screen_title(self, expected_titles):
        title_locator = (AppiumBy.ID, "com.hpx.application:id/screen_title")
        actual_title = self.get_text(title_locator)
        assert actual_title in expected_titles, f"Expected title to be one of {expected_titles}, but got '{actual_title}'"
        return actual_title

class HomePage(BasePage):
    ADD_DEVICE_BUTTON = (AppiumBy.ID, "com.hpx.application:id/add_device_button")
    NAVIGATION_BAR = (AppiumBy.ID, "com.hpx.application:id/navigation_bar")
    DEVICE_LIST_CONTAINER = (AppiumBy.ID, "com.hpx.application:id/device_list_container")
    SETTINGS_ICON = (AppiumBy.ID, "com.hpx.application:id/settings_icon")
    SCREEN_TITLE = (AppiumBy.ID, "com.hpx.application:id/screen_title")
    def verify_home_screen_elements(self):
        self.verify_screen_title(['HPX Home', 'Dashboard', 'My Devices'])
        self.verify_element_visible(self.ADD_DEVICE_BUTTON)
        self.verify_element_enabled(self.ADD_DEVICE_BUTTON)
        self.verify_element_visible(self.NAVIGATION_BAR)
        self.verify_element_visible(self.DEVICE_LIST_CONTAINER)
        self.verify_element_visible(self.SETTINGS_ICON)
        self.verify_element_enabled(self.SETTINGS_ICON)
    def verify_no_devices_configured(self):
        empty_state_locator = (AppiumBy.ID, "com.hpx.application:id/empty_device_list")
        self.verify_element_visible(empty_state_locator)
    def verify_no_shortcuts_exist(self):
        empty_shortcuts_locator = (AppiumBy.ID, "com.hpx.application:id/empty_shortcuts")
        self.verify_element_visible(empty_shortcuts_locator)
    def click_add_device_button(self):
        self.click_element(self.ADD_DEVICE_BUTTON)

class DeviceDetailsPage(BasePage):
    BACK_BUTTON = (AppiumBy.ID, "com.hpx.application:id/back_button")
    DEVICE_NAME_FIELD = (AppiumBy.ID, "com.hpx.application:id/device_name_field")
    DEVICE_TYPE_FIELD = (AppiumBy.ID, "com.hpx.application:id/device_type_field")
    SAVE_BUTTON = (AppiumBy.ID, "com.hpx.application:id/save_button")
    DELETE_BUTTON = (AppiumBy.ID, "com.hpx.application:id/delete_button")
    DEVICE_INFO_SECTION = (AppiumBy.ID, "com.hpx.application:id/device_info_section")
    def verify_device_details_screen(self):
        self.verify_screen_title(['Device Details', 'Device Info'])
        self.verify_element_visible(self.BACK_BUTTON)
        self.verify_element_enabled(self.BACK_BUTTON)
        self.verify_element_visible(self.DEVICE_NAME_FIELD)
        self.verify_element_enabled(self.DEVICE_NAME_FIELD)
        self.verify_element_visible(self.DEVICE_TYPE_FIELD)
        self.verify_element_visible(self.SAVE_BUTTON)
        self.verify_element_enabled(self.SAVE_BUTTON)
        self.verify_element_visible(self.DEVICE_INFO_SECTION)
    def click_back_button(self):
        self.click_element(self.BACK_BUTTON)

class ShortcutsPage(BasePage):
    BACK_BUTTON = (AppiumBy.ID, "com.hpx.application:id/back_button")
    ADD_SHORTCUT_BUTTON = (AppiumBy.ID, "com.hpx.application:id/add_shortcut_button")
    SHORTCUTS_LIST = (AppiumBy.ID, "com.hpx.application:id/shortcuts_list")
    SHORTCUTS_HEADER = (AppiumBy.ID, "com.hpx.application:id/shortcuts_header")
    def verify_shortcuts_screen(self):
        self.verify_screen_title(['Shortcuts', 'My Shortcuts'])
        self.verify_element_visible(self.BACK_BUTTON)
        self.verify_element_enabled(self.BACK_BUTTON)
        self.verify_element_visible(self.ADD_SHORTCUT_BUTTON)
        self.verify_element_enabled(self.ADD_SHORTCUT_BUTTON)
        self.verify_element_visible(self.SHORTCUTS_LIST)
        self.verify_element_visible(self.SHORTCUTS_HEADER)
    def click_add_shortcut_button(self):
        self.click_element(self.ADD_SHORTCUT_BUTTON)
    def click_back_button(self):
        self.click_element(self.BACK_BUTTON)

class AddNewShortcutPage(BasePage):
    BACK_BUTTON = (AppiumBy.ID, "com.hpx.application:id/back_button")
    SHORTCUT_NAME_FIELD = (AppiumBy.ID, "com.hpx.application:id/shortcut_name_field")
    SHORTCUT_ACTION_FIELD = (AppiumBy.ID, "com.hpx.application:id/shortcut_action_field")
    SAVE_BUTTON = (AppiumBy.ID, "com.hpx.application:id/save_button")
    CANCEL_BUTTON = (AppiumBy.ID, "com.hpx.application:id/cancel_button")
    SHORTCUT_CONFIG_SECTION = (AppiumBy.ID, "com.hpx.application:id/shortcut_config_section")
    def verify_add_new_shortcut_screen(self):
        self.verify_screen_title(['Add New Shortcut', 'Create Shortcut', 'New Shortcut'])
        self.verify_element_visible(self.BACK_BUTTON)
        self.verify_element_enabled(self.BACK_BUTTON)
        self.verify_element_visible(self.SHORTCUT_NAME_FIELD)
        self.verify_element_enabled(self.SHORTCUT_NAME_FIELD)
        self.verify_element_visible(self.SHORTCUT_ACTION_FIELD)
        self.verify_element_enabled(self.SHORTCUT_ACTION_FIELD)
        self.verify_element_visible(self.SAVE_BUTTON)
        self.verify_element_enabled(self.SAVE_BUTTON)
        self.verify_element_visible(self.CANCEL_BUTTON)
        self.verify_element_enabled(self.CANCEL_BUTTON)
        self.verify_element_visible(self.SHORTCUT_CONFIG_SECTION)
    def click_back_button(self):
        self.click_element(self.BACK_BUTTON)

def reset_hpx_application_android():
    try:
        result = subprocess.run(
            ['adb', 'shell', 'pm', 'clear', 'com.hpx.application'],
            capture_output=True,
            text=True,
            timeout=10
        )
        assert result.returncode == 0, f"Failed to reset app: {result.stderr}"
        print("HPX application reset successfully (Android)")
    except Exception as e:
        pytest.fail(f"Failed to reset HPX application: {str(e)}")

def reset_hpx_application_ios(driver):
    try:
        driver.terminate_app('com.hpx.application')
        driver.activate_app('com.hpx.application', {'arguments': ['--reset-to-defaults']})
        print("HPX application reset successfully (iOS)")
    except Exception as e:
        pytest.fail(f"Failed to reset HPX application: {str(e)}")

def reset_hpx_application(driver):
    platform_name = driver.capabilities.get('platformName', '').lower()
    if platform_name == 'android':
        reset_hpx_application_android()
    elif platform_name == 'ios':
        reset_hpx_application_ios(driver)
    else:
        pytest.fail(f"Unsupported platform: {platform_name}")

def test_C46(driver):
    print("Step 1: Resetting HPX application to default state...")
    reset_hpx_application(driver)
    driver.activate_app('com.hpx.application')
    home_page = HomePage(driver)
    device_details_page = DeviceDetailsPage(driver)
    shortcuts_page = ShortcutsPage(driver)
    add_new_shortcut_page = AddNewShortcutPage(driver)
    print("Step 2: Verifying home screen elements...")
    home_page.verify_home_screen_elements()
    home_page.verify_no_devices_configured()
    home_page.verify_no_shortcuts_exist()
    print("Step 3: Navigating to Device Details screen...")
    home_page.click_add_device_button()
    device_details_page.verify_device_details_screen()
    device_details_page.click_back_button()
    home_page.verify_home_screen_elements()
    print("Step 4: Navigating to Shortcuts screen...")
    shortcuts_locator = (AppiumBy.ID, "com.hpx.application:id/shortcuts_nav_button")
    home_page.click_element(shortcuts_locator)
    shortcuts_page.verify_shortcuts_screen()
    print("Step 5: Navigating to Add New Shortcuts screen...")
    shortcuts_page.click_add_shortcut_button()
    add_new_shortcut_page.verify_add_new_shortcut_screen()
    add_new_shortcut_page.click_back_button()
    shortcuts_page.verify_shortcuts_screen()
    shortcuts_page.click_back_button()
    home_page.verify_home_screen_elements()
    print("Test Case C46 completed successfully!")
@pytest.fixture
def driver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '12.0',
        'deviceName': 'Android Emulator',
        'app': '/path/to/hpx_application.apk',
        'appPackage': 'com.hpx.application',
        'appActivity': '.MainActivity',
        'automationName': 'UiAutomator2',
        'noReset': False,
        'fullReset': False
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
if __name__ == "__main__":
    pytest.main([__file__, '-v', '-s'])