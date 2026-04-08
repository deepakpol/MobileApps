import pytest

# Assuming the use of a page object model and fixtures as per the mapped scripts
from app.pages.login_page import LoginPage
from app.pages.shortcuts_page import ShortcutsPage
from app.pages.shortcut_edit_page import ShortcutEditPage
from app.pages.delete_confirmation_page import DeleteConfirmationPage

# Global HPX app configuration
pytest.app_info = "HPX"

@pytest.fixture
def setup_printer_and_shortcut(app_driver, user_account):
    """
    Fixture to ensure:
    1. Supported printer is added on the root view.
    2. User is logged into the account.
    3. User has existing shortcuts.
    """
    login_page = LoginPage(app_driver)
    shortcuts_page = ShortcutsPage(app_driver)
    # Log in user
    login_page.login(user_account["username"], user_account["password"])
    # Add printer if not present
    if not shortcuts_page.is_printer_added():
        shortcuts_page.add_supported_printer()
    # Ensure at least one shortcut exists
    if not shortcuts_page.has_shortcuts():
        shortcuts_page.create_shortcut("Test Shortcut")
    yield
    # Teardown if necessary (e.g., remove test shortcut)

def test_delete_shortcut_navigates_and_removes_shortcut(app_driver, setup_printer_and_shortcut):
    """
    Verify the screen, when user clicks on Delete button in pop up window.
    TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/74
    """
    shortcuts_page = ShortcutsPage(app_driver)
    shortcut_name = shortcuts_page.get_first_shortcut_name()
    # Navigate to shortcut edit screen
    shortcut_edit_page = shortcuts_page.open_shortcut_edit(shortcut_name)
    # Click on Delete icon
    shortcut_edit_page.click_delete_icon()
    # Confirm deletion in the confirmation popup
    delete_confirmation_page = DeleteConfirmationPage(app_driver)
    delete_confirmation_page.confirm_delete()
    # Verify navigation to shortcuts screen
    assert shortcuts_page.is_displayed(), "Should navigate back to shortcuts screen"
    # Verify the shortcut is no longer displayed
    assert not shortcuts_page.is_shortcut_present(shortcut_name), f"Shortcut '{shortcut_name}' should be deleted"
