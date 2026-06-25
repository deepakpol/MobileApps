def test_navigate_to_features_screen_verify_smart_security_button(self):
    """
    Test: Navigate to Features screen and verify Smart Security button is displayed
    Priority: P1
    
    Description:
    1. Navigate to Smart Dashboard Features menu (loads HP+ account and opens Features)
    2. Verify Features screen displays the Smart Security button
    
    Expected Result:
    Features screen shows the Smart Security button
    """
    # Step 1: Navigate to Features menu from Smart Dashboard with HP+ account
    self.fc.flow_home_smart_dashboard_features_menu()
    
    # Step 2: Verify Features screen is displayed with Smart Security button
    # verify_features_screen waits for smart_security_btn to be present
    self.fc.flow["features"].verify_features_screen()

def test_navigate_to_other_features_screen(self):
    """
    Test: Navigate to Other Features screen
    Target: HP Connect web features flow
    Priority: P1
    
    Steps:
    1. From Features menu, click Other Features button
    2. Verify Other Features screen displays with title and container
    """
    # TODO: Navigate to Features menu (prerequisite step - method not found in context)
    
    # Click Other Features button
    self.fc.flow["features"].click_other_features_btn()
    
    # Verify Other Features screen displays
    self.fc.flow["features"].verify_other_features_screen()