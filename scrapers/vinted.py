from playwright.sync_api import sync_playwright

def scrape_vinted(search_query):
    url = f"https://www.vinted.de/catalog?search_text={search_query.replace(' ', '+')}"
    print(f"[SCRAPER] Otwieram: {url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector('div.feed-grid__item')

        items = page.query_selector_all('div.feed-grid__item')[:10]
        results = []

        for item in items:
            title = item.query_selector("h3").inner_text() if item.query_selector("h3") else ""
            price = item.query_selector("div.price").inner_text() if item.query_selector("div.price") else ""
            results.append({
                "title": title,
                "price": price
            })

        browser.close()
        return results
