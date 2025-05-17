import openai
import os

def analyze_with_gpt(vinted_data, search_query):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"""
Jesteś ekspertem ds. sprzedaży mody używanej w Niemczech. Na podstawie danych ze stron takich jak Vinted wygeneruj punktową analizę:

1. Co to za produkt (typ, marka, płeć, styl, sezon)?
2. Czy jest dostępny jako nowy? Jeśli nie, ile kosztował?
3. Ceny używane (najniższa, najwyższa, średnia)
4. Propozycja ceny sprzedaży (z uwzględnieniem 15% prowizji i 6 € wysyłki)
5. Podsumowanie: jak wygląda sytuacja tego produktu we Francji i Polsce

Dane znalezione na Vinted:
{vinted_data}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Jesteś analitykiem cen odzieży używanej w Niemczech."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )

    return response.choices[0].message.content
