import pytest
from pages.hpx_shortcuts import HpxShortcuts

def test_C46(driver):
    # Step 1: Reset HPX application to default state and ensure user is logged in before launching.
    # TODO: UNMAPPED STEP → Reset HPX application to default state and ensure user is logged in before launching.

    # Step 2: Add supported printer device via 'Add Device' button on root view screen, searching by IP address, and verify printer is listed and ready.
    # TODO: UNMAPPED STEP → Add supported printer device via 'Add Device' button on root view screen, searching by IP address, and verify printer is listed and ready.

    # Step 3: After each navigation (root view, device details, shortcuts screen, add new shortcuts screen), assert that the expected screen title and main UI elements are visible and correctly rendered for early failure detection.
    page = HpxShortcuts(driver)
    assert page.verify_shortcuts_screen_title(timeout=10, raise_e=True)
    assert page.verify_edit_shortcuts_screen_title(timeout=10, raise_e=True)
    assert page.verify_add_new_shortcut_screen_title(timeout=10, raise_e=True)
