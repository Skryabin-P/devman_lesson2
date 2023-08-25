import requests
import json
from urllib.parse import urlparse
import os
from dotenv import load_dotenv


def shorten_link(token: str, link: str):
    header = {'Authorization': f'Bearer {token}'}
    endpoint = 'v4/bitlinks'
    api_url = 'https://api-ssl.bitly.com/' + endpoint
    payload = {"long_url": link}
    response = requests.post(api_url, headers=header, json=payload)
    response.raise_for_status()
    new_bitlink = response.json()
    new_bitlink_url = new_bitlink["link"]
    return new_bitlink_url


def count_clicks(token: str, link: str):
    header = {'Authorization': f'Bearer {token}'}
    endpoint = 'v4/bitlinks/'
    parsed_bitlink = urlparse(link)
    bitlink = f'{parsed_bitlink.netloc}{parsed_bitlink.path}'
    api_url = f'https://api-ssl.bitly.com/{endpoint}/{bitlink}/clicks/summary'
    payload = {"unit": "day", "units": -1}
    response = requests.get(api_url, headers=header, params=payload)
    response.raise_for_status()
    bitlink_stats = response.json()
    clicks_number = bitlink_stats['total_clicks']
    return clicks_number


def is_bitlink(token: str, url: str):
    parsed_url = urlparse(url)
    header = {'Authorization': f'Bearer {token}'}
    endpoint = 'v4/bitlinks/'
    bitlink = f'{parsed_url.netloc}{parsed_url.path}'
    response = requests.get(f'https://api-ssl.bitly.com/{endpoint}{bitlink}',
                            headers=header)
    return response.ok


def main():
    load_dotenv()
    bitly_api_token = os.environ['BITLY_API_TOKEN']
    link = input("Enter your url address:")

    if is_bitlink(bitly_api_token, link):
        try:
            clicks_number = count_clicks(bitly_api_token, link)
            print(f'Total clicks on {link} is {clicks_number}')
        except requests.exceptions.HTTPError as error:
            print(f'Remote host returns an error :\n {error}')
    else:
        try:
            bitlink = shorten_link(bitly_api_token, link)
            print("Your Bitlink is", bitlink)
        except requests.exceptions.HTTPError as error:
            print(f'Remote host returns an error :\n {error}')


if __name__ == "__main__":
    main()
