from playwright.sync_api import Page, expect


BASE_URL = "http://localhost:8000/"


def test_five_cubed(page: Page):
    page.goto(BASE_URL)

    input = page.get_by_placeholder("enter number...")
    input.fill("5")

    page.get_by_role(
        "button", name="Cube"
    ).click()

    result = page.locator("css=p#result")

    expect(result).to_contain_text("125")


def test_empty_input(page: Page):
    page.goto(BASE_URL)

    input = page.get_by_placeholder("enter number...")
    input.fill("")

    page.get_by_role(
        "button", name="Cube"
    ).click()

    result = page.locator("css=p#result")

    expect(result).to_have_text(
        "Enter something!"
    )