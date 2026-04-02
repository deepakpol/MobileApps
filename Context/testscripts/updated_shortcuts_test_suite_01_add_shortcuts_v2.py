import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time
import logging

pytest.app_info = "HPX"

class Test_Suite_01_Add_Shortcut(object):
    # GLOBAL MISTAKE: Missing autouse=True
    @pytest.fixture(scope="class") 
    def class_setup(cls, request, android_hpx_flow_setup ,load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_hpx_flow_setup
        cls.p = load_printers_session
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.hpx_shortcuts = cls.fc.fd[FLOW_NAMES.HPX_SHORTCUTS]
        cls.fc.hpx = True
        logging.info("Starting Test Suite 01 for HPX Add Shortcuts")

    def test_01_verify_the_screen_when_user_clicks_on_the_create_your_own_shortcut_arrow_button_in_add_new_shortcuts_screen_C46(self):
        """
        Verify the screen.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/46
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        assert self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        assert self.hpx_shortcuts.verify_add_new_shortcut_screen_title()

    def test_02_verify_the_screen_when_user_clicks_on_the_back_button_in_add_shortcut_screen_C47(self):
        """
        Verify the pop up screen.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/47
        """
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_cancel_shortcut_go_back_btn()
        assert self.hpx_shortcuts.verify_cancel_this_shortcut_title()
    
    def test_03_verify_the_position_of_the_buttons_on_the_cancel_shortcut_creation_pop_up_window_C48(self):
        """
        Verify the buttons of cancel shortcut creation pop up window.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/48
        """
        assert self.hpx_shortcuts.verify_add_new_shortcut_screen_title()
        assert self.hpx_shortcuts.verify_cancel_shortcut_go_back_btn()
    
    def test_04_verify_the_screen_when_the_user_clicks_on_go_back_button_C49(self):
        """
        Verify the screen when user clicks go back.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/49
        """
        assert self.hpx_shortcuts.verify_add_new_shortcut_screen_title()
        self.hpx_shortcuts.click_cancel_shortcut_go_back_btn()
        assert self.hpx_shortcuts.verify_add_new_shortcut_title()

    def test_05_verify_the_screen_when_user_clicks_on_the_yes_cancel_button_C50(self):
        """
        Verify the screen when user clicks yes cancel.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/50
        """
        self.hpx_shortcuts.click_cancel_shortcut_go_back_btn()
        assert self.hpx_shortcuts.verify_cancel_this_shortcut_title()
        self.hpx_shortcuts.click_cancel_shortcut_yes_cancel_btn()
    
    def test_06_verify_the_behavior_when_user_enables_the_print_destination_toggle_bar_in_add_shortcut_screen_C51(self):
        """
        Verify the behavior when user enables the print destination toggle bar.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/51
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        assert self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        assert self.hpx_shortcuts.verify_add_new_shortcut_screen_title()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        assert self.hpx_shortcuts.is_continue_btn_enabled(), "Continue button should be enabled after toggling print option"