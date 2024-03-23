import requests
from requests.exceptions import RequestException
from pathlib import Path
import logging

FILEPATH = Path(__file__).parent / "airbnb.html"
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


def fetch_content(url: str, from_disk: bool = False) -> str:
    if from_disk and FILEPATH.exists():
        return _read_from_file()
    try:
        logger.debug(f"Fetching content from {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html_content = response.text
        _write_to_file(content=html_content)
        return html_content
    except RequestException as e:
        logger.error(f"Failed to fetch content from {url}: due to {str(e)}")
        raise e


def _write_to_file(content: str) -> bool:
    logger.debug(f"Writing content to file: {FILEPATH}")
    with open(FILEPATH, "w") as file:
        file.write(content)
    return FILEPATH.exists()


def _read_from_file() -> str:
    logger.debug(f"Reading content from file: {FILEPATH}")
    with open(FILEPATH, "r") as file:
        return file.read()


if __name__ == '__main__':
    url = "https://www.booking.com/searchresults.en-gb.html?ss=Somone&ssne=Somone&ssne_untouched=Somone&label=en-fr-booking-desktop-Akb7DsuMl_04Kj1fagYeEgS652796016858%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9056455%3Ali%3Adec%3Adm&aid=2311236&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=-2274637&dest_type=city&checkin=2024-04-01&checkout=2024-04-06&group_adults=2&no_rooms=1&group_children=0"
    content = fetch_content(url=url, from_disk=True)
    print(content)

# pip install --upgrade pip
# pip install beautifulsoup4
# pip install requests
# pip install playwright
# executer cette commande après l'installation : $ playwright install