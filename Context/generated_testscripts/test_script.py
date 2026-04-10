from pages.hpx_shortcuts import HpxShortcuts


def test_C46(driver):
    # Step 1: Reset the HPX application to its default state using the automation command 'adb shell pm clear com.hpx.application' (Android) or by launching with '--reset-to-defaults' argument (iOS), and verify that no devices are configured and no shortcuts exist.
    # TODO: UNMAPPED STEP → Reset the HPX application to its default state using the automation command 'adb shell pm clear com.hpx.application' (Android) or by launching with '--reset-to-defaults' argument (iOS), and verify that no devices are configured and no shortcuts exist.

    # Step 2: After launching the HPX app, assert that the screen title is 'HPX Home', 'Dashboard', or 'My Devices', and verify the presence and visibility of the Add Device button, navigation bar, device list container, and settings icon.
    # TODO: UNMAPPED STEP → After launching the HPX app, assert that the screen title is 'HPX Home', 'Dashboard', or 'My Devices', and verify the presence and visibility of the Add Device button, navigation bar, device list container, and settings icon.

    # Step 3: After each navigation (to Device Details, Shortcuts screen, Add New Shortcuts screen), assert the expected screen title and verify all main UI elements for that screen are visible and enabled, including back button, relevant input fields, action buttons, and section headers.
    page = HpxShortcuts(driver)
    assert page.verify_shortcuts_screen_title(timeout=10, raise_e=True)
    assert page.verify_add_new_shortcut_btn(timeout=10, raise_e=True)
    assert page.verify_shortcuts_edit_btn(timeout=10, raise_e=True)
    assert page.verify_shortcuts_settings_icon(timeout=10, raise_e=True)
    assert page.verify_add_new_shortcut_screen_title(timeout=10, raise_e=True)
    assert page.verify_edit_shortcuts_screen_title(timeout=10, raise_e=True)
