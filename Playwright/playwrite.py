from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.cricbuzz.com.")
    page.screenshot(path="screenshot.png")
    print("Extracting the page")
    try:
        score=page.locator("div.cb-col.cb-col-100.cb-ltst-wgt-hdr").first.inner_text()
        score.wait_for(state="visible", timeout=5000)
        print("Score:", score.inner_text())
    except Exception as e:
        print("No live match occured")
    page.screenshot(path="live_score.png")
    browser.close()