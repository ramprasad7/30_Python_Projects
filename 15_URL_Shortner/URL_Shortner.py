from typing import Final
import requests


API_KET: Final[str] = "2da9cc7560531b2a3dd91603bcee9649cae19"
BASE_URL: Final[str] = "https://cutt.ly/api/api.php"

def shorten_link(full_url: str):
    payload: dict = {'key': API_KET, 'short': full_url}
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    if url_data := data.get('url'):
        if url_data['status'] == 7:
            short_link: str = url_data['shortLink']
            print(f"Link: {short_link}")

        else:
            print(f"Error Status: {url_data['status']}")




def main():
    input_link: str = input("Enter the URL: ")
    shorten_link(input_link)

if __name__ == '__main__':
    main()