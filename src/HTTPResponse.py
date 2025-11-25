from urllib.request import urlopen
import json
from pprint import pprint

_HTTP_URL = "http://example.com"
_JSON_URL = "https://jsonplaceholder.typicode.com/todos/1"

def pprint_http_response(url=_HTTP_URL):
    with urlopen(url) as response:
        pprint(dir(response))

def fetch_http(url=_HTTP_URL):
    with urlopen(url) as response:
        body = response.read()
    
    return body

def print_first_15_chars_from_http():
    body = fetch_http()
    return body[:15]

def fetch_json(url=_JSON_URL):
    with urlopen(url) as response:
        body = response.read()
    
    data = json.loads(body)
    return data

if __name__ == "__main__":
    print("PRINTING FIRST 15 CHARS FROM HTTP RESPONSE")
    print(print_first_15_chars_from_http())
    print("\nPRINTING JSON DATA")
    print(fetch_json())
    print("\nPPRINTING HTTP RESPONSE ATTRIBUTES")
    pprint_http_response(_HTTP_URL)