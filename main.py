import requests


def get_price():
    url = "https://www.airbnb.fr/s/Dakar--S%C3%A9n%C3%A9gal/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-04-01&monthly_length=3&monthly_end_date=2024-07-01&price_filter_input_type=0&channel=EXPLORE&query=Dakar%2C%20S%C3%A9n%C3%A9gal&place_id=ChIJcbvFs_VywQ4RH7JdLdkXfLE&date_picker_type=calendar&checkin=2024-04-02&checkout=2024-04-12&source=structured_search_input_header&search_type=autocomplete_click"
    response = requests.get(url)
    print(response.text)


if __name__ == '__main__':
    get_price()

# pip install --upgrade pip
# pip install beautifulsoup4
# pip install requests
# pip install playwright
# executer cette commande après l'installation : $ playwright install