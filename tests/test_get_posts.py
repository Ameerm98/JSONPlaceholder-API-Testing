import pytest
from http import HTTPStatus
from API.jsonplaceholder_API import JSONPlaceholderAPI
from API import utils
from tests.data.tests_data import (
    VALID_POST_ID,
    INVALID_POST_ID,
    USER_ID,
    ID,
    TITLE,
    BODY,
    POST_TITLE,
    POST_BODY,
    NON_EXIST_POST_ID,
    NEGATIVE_POST_ID
)


def get_api_client():
    """Return an instance of the JSONPlaceholder API client."""
    return JSONPlaceholderAPI()


class TestGETPosts:
    client = get_api_client()

    def test_get_posts(self):
        """Test retrieving the full list of posts."""
        resp = self.client.get_posts()
        posts = utils.get_response_content(resp)

        # Ensure we receive an HTTP 200 OK response
        assert resp.status_code == HTTPStatus.OK, f"Expected 200 OK, got {resp.status_code}"

        # Ensure the response is a list (i.e., a list of posts)
        assert isinstance(posts, list), "Expected response content to be a list of posts"

    def test_get_post_with_valid_id(self):
        """Test retrieving a single post by a valid ID."""
        resp = self.client.get_post(VALID_POST_ID)
        valid_post = utils.get_response_content(resp)

        # Ensure we receive an HTTP 200 OK response
        assert resp.status_code == HTTPStatus.OK, f"Expected 200 OK, got {resp.status_code}"

        # Ensure the response is a dictionary object
        assert isinstance(valid_post, dict), "Expected response content to be a single post (dict)"

        # Ensure the 'userId' field exists and is the expected integer
        assert USER_ID in valid_post, "'userId' key is missing in the response"
        assert isinstance(valid_post[USER_ID], int), "'userId' should be an integer"
        assert valid_post[USER_ID] == VALID_POST_ID, f"Expected userId {VALID_POST_ID}, got {valid_post[USER_ID]}"

        # Ensure the 'id' field exists and is correct
        assert ID in valid_post, "'id' key is missing in the response"
        assert isinstance(valid_post[ID], int), "'id' should be an integer"
        assert valid_post[ID] == VALID_POST_ID, f"Expected id {VALID_POST_ID}, got {valid_post[ID]}"

        # Ensure the 'title' field exists and matches expected value
        assert TITLE in valid_post, "'title' key is missing in the response"
        assert isinstance(valid_post[TITLE], str), "'title' should be a string"
        assert valid_post[TITLE] == POST_TITLE, "Title does not match expected value"

        # Ensure the 'body' field exists and matches expected value
        assert BODY in valid_post, "'body' key is missing in the response"
        assert isinstance(valid_post[BODY], str), "'body' should be a string"
        assert valid_post[BODY] == POST_BODY, "Body does not match expected value"

    def test_get_posts_with_invalid_id(self):
        """Test retrieving a post with a non-numeric or malformed ID."""
        resp = self.client.get_post(INVALID_POST_ID)

        # Expecting a 404 Not Found for invalid post ID format
        assert resp.status_code == HTTPStatus.NOT_FOUND, f"Expected 404 Not Found, got {resp.status_code}"

    def test_get_post_non_exist_id(self):
        """Test retrieving a post with a valid format but non-existent ID."""
        resp = self.client.get_post(NON_EXIST_POST_ID)

        # Should return 404 Not Found if the ID doesn't exist
        assert resp.status_code == HTTPStatus.NOT_FOUND, f"Expected 404 Not Found, got {resp.status_code}"

    def test_get_post_negative_id(self):
        """Test retrieving a post with a negative ID (invalid)."""
        resp = self.client.get_post(NEGATIVE_POST_ID)

        # Negative IDs should result in 404 Not Found
        assert resp.status_code == HTTPStatus.NOT_FOUND, f"Expected 404 Not Found, got {resp.status_code}"
