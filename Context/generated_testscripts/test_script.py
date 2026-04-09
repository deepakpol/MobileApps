import pytest
from pages.AddDevice import AddDevice


def test_C46(driver):
    # Step 1: Reset HPX application to default state and ensure user is logged in before launching.
    # TODO: UNMAPPED STEP → Reset HPX application to default state and ensure user is logged in before launching.

    # Step 2: Add supported printer device via 'Add Device' button on root view screen, searching by IP address, and verify printer is listed and ready.
    # TODO: UNMAPPED STEP → Add supported printer device via 'Add Device' button on root view screen, searching by IP address, and verify printer is listed and ready.

    # Step 3: After each navigation (root view, device details, shortcuts screen, add new shortcuts screen), assert that the expected screen title and main UI elements are visible and correctly rendered for early failure detection.
    page = AddDevice(driver)
    assert page.verify_add_device_page(), "Add Device page elements are not visible."
