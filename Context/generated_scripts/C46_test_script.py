import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time
import logging
pytest.app_info = "HPX"

@pytest.fixture(scope="class")
def class_setup(cls, request, android_hpx_flow_setup, load_printers_session):
    cls = cls.__class__
    cls.driver, cls.fc = android_hpx_flow_setup
    cls.p = load_printers_session
    cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
    cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
    cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
    cls.hpx_shortcuts = cls.fc.fd[FLOW_NAMES.HPX_SHORTCUTS]
    cls.fc.hpx = True
    logging.info("Starting Test Suite 01 for HPX Add Shortcuts")

class TestHPXAddShortcuts(object):

    def test_01_verify_the_screen_when_user_clicks_on_the_create_your_own_shortcut_arrow_button_in_add_new_shortcuts_screen_C46(self):
        """
        Verify the screen.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/46

        Steps:
            1. Install and Launch the HPX app.
            2. Click on the printer icon on the root view screen.
            3. Then click on the shortcuts tile on the device details page.
            4. Click on Add new shortcuts in shortcuts screen.
            5. The click on the Create your own shortcut arrow button.
            6. Verify the screen.

        Expected Result:
            User should be navigated to the 'Add shortcut' screen.
        """
        # Implicit Step – Required for Test Execution: Reset application to initial state
        self.fc.reset_app()

        # Step 1: Install and Launch the HPX app.
        self.fc.flow_load_home_screen(skip_value_prop=False)

        # Implicit Step – Required for Test Execution: Add printer device (Precondition)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)

        # Step 2: Click on the printer icon on the root view screen.
        self.hpx_printer_details.click_printer_device_card()

        # Step 3: Then click on the shortcuts tile on the device details page.
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)

        # Supporting Step – Purpose of Test Case Validation: Verify shortcuts screen is displayed
        assert self.hpx_shortcuts.verify_shortcuts_screen_title()

        # Step 4: Click on Add new shortcuts in shortcuts screen.
        self.hpx_shortcuts.click_add_new_shortcut_btn()

        # Step 5: The click on the Create your own shortcut arrow button.
        # Step 6: Verify the screen.
        assert self.hpx_shortcuts.verify_add_new_shortcut_screen_title()