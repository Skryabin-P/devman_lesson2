import requests
import json
from urllib.parse import urlparse
import os
from dotenv import load_dotenv


def short_link(token: str, link: str):
    header = {'Authorization': f'Bearer {token}',
              'Content-Type': 'application/json'}
    endpoint = 'v4/bitlinks'
    api_url = 'https://api-ssl.bitly.com/' + endpoint
    payload = {"long_url": link}
    response = requests.post(api_url, headers=header, json=payload)
    response.raise_for_status()
    json_data = response.json()
    bitlink = json_data["link"]
    return bitlink


def count_clicks(token: str, link: str):
    header = {'Authorization': f'Bearer {token}'}
    endpoint = 'v4/bitlinks/'
    parsed_bitlink = urlparse(link)
    bitlink = parsed_bitlink.netloc+parsed_bitlink.path
    api_url = f'https://api-ssl.bitly.com/{endpoint}/{bitlink}/clicks/summary'
    payload = {"unit": "day", "units": -1}
    response = requests.get(api_url, headers=header, params=payload)
    response.raise_for_status()
    json_data = response.json()
    clicks_number = json_data['total_clicks']
    return clicks_number


def is_bitlink(url: str):
    parsed_url = urlparse(url)
    if parsed_url.netloc == "bit.ly":
        return True
    return False


if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.environ['TOKEN']
    link = str(input("Enter your url address:"))

    if is_bitlink(link):
        try:
            clicks_number = count_clicks(TOKEN, link)
            print(f'Total clicks on {link} is {clicks_number}')
        except requests.exceptions.HTTPError as error:
            print(f'Remote host returns an error :\n {error}')
    else:
        try:
            bitlink = short_link(TOKEN, link)
            print("Your Bitlink is", bitlink)
        except requests.exceptions.HTTPError as error:
            print(f'Remote host returns an error :\n {error}')
