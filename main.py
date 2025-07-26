from playwright.sync_api import sync_playwright

# Sample code to login to facebook account
def fb_login(playwright):
    browser = playwright.chromium.launch(headless=False)  
    page = browser.new_page()

    page.goto("https://www.facebook.com/login.php")

    username = "your_email_or_phone"
    password = "your_password"

    # Fill in login form
    page.fill('input[name="email"]', username)
    page.fill('input[name="pass"]', password)

    # Click the login button
    page.click('button[name="login"]')

    # Timeout is in milliseconds
    page.wait_for_timeout(10000)  

    browser.close()

with sync_playwright() as playwright:
    fb_login(playwright)
