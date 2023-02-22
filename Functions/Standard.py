#!python3.8
from json import loads
from requests import post, get
from typing import Tuple, Union
from config import items

BASE_URL = items["mine"]

auth_url_base = ''.join((items["mine"], items["auth"]))
api_url_base = ''.join((items["mine"], items["api"]))

tokens = get_tokens(login=items["user"], password=items["pass"])

    if not tokens:
        print("Authentication failed")
        return

headers['ABC'] = f'Bearer {access_token}'

if __name__ == '__main__':
    res = main()
    print(f'Result : {res}')
