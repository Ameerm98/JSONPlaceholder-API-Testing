import requests


def get_response_content(response: requests.Response):
    return response.json()
