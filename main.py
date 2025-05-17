from scrapers.vinted import scrape_vinted
from gpt.vision_request import analyze_with_gpt
from telegram.send_message import send_to_telegram
import os

def main():
    print("[START] Uruchamiam scraper Vinted...")

    search_query = os.getenv("SEARCH_QUERY", "Nike Air Max 270 Herren 43")
    vinted_data = scrape_vinted(search_query)

    print("[INFO] Przesyłam dane do GPT-4...")
    gpt_response = analyze_with_gpt(vinted_data, search_query)

    print("[INFO] Wysyłam wynik na Telegram...")
    send_to_telegram(gpt_response)

if __name__ == "__main__":
    main()
