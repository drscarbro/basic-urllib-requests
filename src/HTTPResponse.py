from urllib.request import urlopen
import json
from pprint import pprint
from pathlib import Path

_HTTP_URL = "http://example.com"
_JSON_URL = "https://jsonplaceholder.typicode.com/todos/1"
_JSON_HTTP_BIN_URL = "https://httpbin.org/json"
_GOOGLE_URL = "https://www.google.com"
_DEFAULT_CHARSET = "utf-8"


def set_file_path(file_name: str) -> Path:
    file_path = Path(__file__).parent / "files" / file_name
    print(f"File will be saved to: {file_path}")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    return file_path


def get_http_response_header_using_charset(url=_HTTP_URL):
    with urlopen(url) as response:
        body = response.read()

    charset = response.headers.get_content_charset()
    if charset:
        print(f"Using charset found in headers: {charset}")
    else:
        print("No charset found in headers; defaulting to 'utf-8'")
        charset = "utf-8"

    text = body.decode(charset)
    return text


def get_http_response_header_charset(url=_HTTP_URL):
    with urlopen(url) as response:
        body = response.read()

    charset = response.headers.get_content_charset()
    if charset:
        print(f"Using charset found in headers: {charset}")
        return charset
    else:
        print("No charset found in headers; defaulting to 'utf-8'")
        charset = "utf-8"
    return charset


def from_bytes_to_strings(url=_HTTP_URL):
    with urlopen(url) as response:
        body = response.read()

    text = body.decode("utf-8")
    return text


def pprint_http_response(url=_HTTP_URL):
    with urlopen(url) as response:
        pprint(dir(response))


def fetch_http(url=_HTTP_URL):
    with urlopen(url) as response:
        body = response.read()

    return body


def print_first_15_chars_from_http(url=_HTTP_URL):
    body = fetch_http(url)
    return body[:15]


def fetch_json(url=_JSON_URL):
    with urlopen(url) as response:
        body = response.read()

    data = json.loads(body)
    return data


def write_http_response_to_file(file="http_response.html", url=_HTTP_URL):
    file_path = set_file_path(file)
    body = fetch_http(url)
    with open(file_path, "wb") as file:
        file.write(body)


def write_google_response_to_file(file="google_response.html"):
    file_path = set_file_path(file)
    body = get_http_response_header_using_charset(_GOOGLE_URL)
    with open(file_path, encoding=_DEFAULT_CHARSET, mode="w") as file:
        file.write(body)


def get_json_from_http_bin_url(url=_JSON_HTTP_BIN_URL):
    with urlopen(url) as response:
        body = response.read()

    print(type(body))  # Should be bytes
    data = json.loads(body)
    print(type(data))  # Should be dict
    return data


if __name__ == "__main__":
    # print("PRINTING FIRST 15 CHARS FROM HTTP RESPONSE")
    # print(print_first_15_chars_from_http())
    # print("\nPRINTING JSON DATA")
    # print(fetch_json())
    # print("\nPPRINTING HTTP RESPONSE ATTRIBUTES")
    # pprint_http_response(_HTTP_URL)
    # print("CONVERTING HTTP RESPONSE BYTES TO STRINGS")
    # bytes_to_string = from_bytes_to_strings()
    # pprint(bytes_to_string[:30])
    # print("PRINTING HTTP RESPONSE HEADERS CHARSET")
    # print(get_http_response_header_charset(_GOOGLE_URL))
    # print("PRINTING HTTP RESPONSE USING HEADER CHARSET")
    # response = get_http_response_header_using_charset()
    # print(response[:30])
    print("WRITING HTTP RESPONSE TO FILE 'http_response.html'")
    write_http_response_to_file()
    # print("WRITING GOOGLE RESPONSE TO FILE 'google_response.html'")
    # write_google_response_to_file()
    # print("GETTING JSON FROM URL")
    # json_data = get_json_from_http_bin_url()
    # pprint(json_data)
