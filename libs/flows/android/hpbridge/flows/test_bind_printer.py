"""
Unit tests for BindPrinter flow verify_printer_name_matches method.
Pattern modeled on existing hpbridge test conventions.
"""
import unittest
from unittest.mock import Mock, MagicMock
from libs.flows.android.hpbridge.flows.bind_printer import BindPrinter


class TestBindPrinterVerifyName(unittest.TestCase):
    """Test cases for verify_printer_name_matches method."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_driver = Mock()
        self.mock_driver.logger = Mock()
        self.bind_printer = BindPrinter(self.mock_driver)
    
    def test_verify_printer_name_matches_returns_true_when_names_match(self):
        """Test that verify_printer_name_matches returns True when displayed name matches expected."""
        expected_name = "HP LaserJet Pro"
        self.mock_driver.get_text.return_value = expected_name
        
        result = self.bind_printer.verify_printer_name_matches(expected_name)
        
        self.assertTrue(result)
        self.mock_driver.get_text.assert_called_once_with(self.bind_printer._printer_name_text)
        self.mock_driver.logger.info.assert_called()
    
    def test_verify_printer_name_matches_returns_false_when_names_differ(self):
        """Test that verify_printer_name_matches returns False when displayed name differs from expected."""
        expected_name = "HP LaserJet Pro"
        displayed_name = "HP OfficeJet"
        self.mock_driver.get_text.return_value = displayed_name
        
        result = self.bind_printer.verify_printer_name_matches(expected_name)
        
        self.assertFalse(result)
        self.mock_driver.get_text.assert_called_once_with(self.bind_printer._printer_name_text)
    
    def test_verify_printer_name_matches_logs_verification_attempt(self):
        """Test that verify_printer_name_matches logs the verification attempt."""
        expected_name = "HP Printer"
        self.mock_driver.get_text.return_value = expected_name
        
        self.bind_printer.verify_printer_name_matches(expected_name)
        
        # Verify logging was called with expected name
        log_calls = [str(call) for call in self.mock_driver.logger.info.call_args_list]
        self.assertTrue(any(expected_name in call for call in log_calls))
    
    def test_verify_printer_name_matches_logs_displayed_name(self):
        """Test that verify_printer_name_matches logs the displayed name."""
        expected_name = "HP LaserJet"
        displayed_name = "HP OfficeJet Pro"
        self.mock_driver.get_text.return_value = displayed_name
        
        self.bind_printer.verify_printer_name_matches(expected_name)
        
        # Verify displayed name was logged
        log_calls = [str(call) for call in self.mock_driver.logger.info.call_args_list]
        self.assertTrue(any(displayed_name in call for call in log_calls))
    
    def test_verify_printer_name_matches_handles_empty_string(self):
        """Test that verify_printer_name_matches handles empty string comparison."""
        expected_name = ""
        self.mock_driver.get_text.return_value = ""
        
        result = self.bind_printer.verify_printer_name_matches(expected_name)
        
        self.assertTrue(result)
    
    def test_verify_printer_name_matches_case_sensitive(self):
        """Test that verify_printer_name_matches performs case-sensitive comparison."""
        expected_name = "HP LaserJet Pro"
        displayed_name = "hp laserjet pro"
        self.mock_driver.get_text.return_value = displayed_name
        
        result = self.bind_printer.verify_printer_name_matches(expected_name)
        
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
