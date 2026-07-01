# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility

pytest.app_info = "hpbridge"


class TestURLPrintContinuePrintButton(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup
        # cls.p = load_printers_session

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mphome = self.fc.flow["mp_home"]
        self.binding = self.fc.flow["bind_printer"]
        self.printsetting = self.fc.flow["print_setting"]
        self.urlprint = self.fc.flow["url_print"]

        # Define variables
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()
        self.url = "https://www.toutiao.com/a6807696360565948942/"
        """
        Pre-conditions:
            1. User has bound one or more printers.
            2. User has bound Baidu accout.
            3. User has followed the related public acccount.
        """
    def test_01_url_print_continue_print(self):
        """
        Steps:
            1. On Applet home page.
            2. Click on "网络文章打印" button in "多功能打印" section.
            3. Perform URL print flow and then print it.
            4. Click on "继续打印" button in "任务提交成功" page, and check the result.
        Expected result:
            Verify the "任务提交成功" page is displayed. And two buttons "继续打印" and "返回首页" are displayed in this page.
            Verify user will return to "网络文章打印" home page (without pasting url) after clicking "继续打印" button.
        """
        # printer = utlitiy_misc.load_printer()
        # self.wechat.send_qrcode(printer["index"])
        self.wechat.send_qrcode(qrcode_index=0)
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.urlprint.click_url_article_print()
        self.urlprint.check_if_reminder_pop_out()
        self.urlprint.input_url_into_field(self.url)
        self.urlprint.get_article()
        self.urlprint.back_from_print_preview()
        self.urlprint.click_goahead_print()
        self.printsetting.select_collapse_button()
        self.printsetting.select_print()
        self.printsetting.click_continue_print_btn()
        self.urlprint.verify_web_article_page_ui()

    def test_02_url_print_back_home_button(self):
        """
        Steps:
            1. On Applet home page.
            2. Click on "网络文章打印" button in "多功能打印" section.
            3. Perform URL print flow and then print it.
            4. Click on "返回首页" button in "任务提交成功" page, and check the result.
        Expected result:
            Verify the "任务提交成功" page is displayed. And two buttons "继续打印" and "返回首页" are displayed in this page.
            Verify user will return to Applet home page after clicking "返回首页" button.
        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.urlprint.click_url_article_print()
        self.urlprint.check_if_reminder_pop_out()
        self.urlprint.input_url_into_field(self.url)
        self.urlprint.get_article()
        self.urlprint.back_from_print_preview()
        self.urlprint.click_goahead_print()
        self.printsetting.select_collapse_button()
        self.printsetting.select_print()
        self.printsetting.click_return_home_btn()
        self.mphome.verify_home_page_displayed()

    def test_03_url_print_top_back_button(self):
        """
        Steps:
            1. On Applet home page.
            2. Click on "网络文章打印" button in "多功能打印" section.
            3. Perform URL print flow and then print it.
            4. Click on "Back" in button in "任务提交成功" page, and check the result.
        Expected result:
            Verify the "任务提交成功" page is displayed. And two buttons "继续打印" and "返回首页" are displayed in this page.
            Verify user will return to "网络文章打印" home page (without pasting url) after clicking "Back" button.
        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.urlprint.click_url_article_print()
        self.urlprint.check_if_reminder_pop_out()
        self.urlprint.input_url_into_field(self.url)
        self.urlprint.get_article()
        self.urlprint.back_from_print_preview()
        self.urlprint.click_goahead_print()
        self.printsetting.select_collapse_button()
        self.printsetting.select_print()
        self.printsetting.click_top_left_back_btn()
        self.urlprint.verify_web_article_page_ui()

    def test_url_print_continue_print_button(self):
        """
        Test that the continue-print button is available after a URL print
        and behaves correctly when used.

        Covers:
        - SDD-55: HP Bridge: Print from URL
        - Behaviour 1: The continue-print button is available after a URL print
        - Behaviour 2: The continue-print button behaves correctly when used

        Steps:
        1. Navigate to URL article print section
        2. Input a valid URL
        3. Get the article
        4. Proceed to print settings
        5. Submit the print job
        6. Verify continue-print button is available and click it
        7. Verify the button behaves correctly (navigates back to print settings)
        """
        # Navigate to URL print
        self.fc.flow["url_print"].click_url_article_print()

        # Input a valid URL
        test_url = "https://www.example.com/article"
        self.fc.flow["url_print"].input_url_into_field(test_url)

        # Get the article
        self.fc.flow["url_print"].get_article()

        # Proceed to print
        self.fc.flow["url_print"].process_to_print()

        # Verify we're on print settings page
        self.fc.flow["print_setting"].verify_print_setting_page()

        # Submit the print job
        self.fc.flow["print_setting"].select_print()

        # Verify job submitted successfully
        self.fc.flow["print_setting"].verify_job_success_submitted_msg()

        # Click continue print button (this verifies availability and clicks it)
        self.fc.flow["print_setting"].click_continue_print_btn()

        # Verify we're back on print settings page (continue-print behaves correctly)
        self.fc.flow["print_setting"].verify_print_setting_page()

