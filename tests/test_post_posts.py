import pytest
from http import HTTPStatus
from API.jsonplaceholder_API import JSONPlaceholderAPI
from API import utils
from tests.data.tests_data import (
    NEW_POST,
    ID,
    TITLE,
    BODY,
    NEW_POST_ID,
    NEW_POST_TITLE,
    POST_MISSING_FIELDS,
    NULL_POST
)


def API():
    """Provide an API client instance for POST tests."""
    return JSONPlaceholderAPI()


class TestPOSTPosts:
    client = API()

    def test_post_posts(self):
        """
        Test case: Creating a new post with all required fields.
        JSONPlaceholder always returns a successful creation (201 Created),
        and echoes back the post content along with a new ID.
        """
        resp = self.client.create_post(NEW_POST)
        new_post = utils.get_response_content(resp)

        # Ensure response status code indicates successful creation
        assert resp.status_code == HTTPStatus.CREATED, f"Expected 201 Created, got {resp.status_code}"

        # Response must be a dictionary representing the new post
        assert isinstance(new_post, dict), "Expected response to be a dict"

        # Ensure the response includes an 'id' field and it is the expected integer
        assert ID in new_post, "'id' key missing in response"
        assert isinstance(new_post[ID], int), "'id' should be an integer"
        assert new_post[ID] == NEW_POST_ID, f"Expected id {NEW_POST_ID}, got {new_post[ID]}"

        # Ensure the 'title' field is present and matches the request payload
        assert TITLE in new_post, "'title' key missing in response"
        assert isinstance(new_post[TITLE], str), "'title' should be a string"
        assert new_post[TITLE] == NEW_POST_TITLE, "Title does not match posted title"

        # Ensure the 'body' field is present and matches the request payload
        assert BODY in new_post, "'body' key missing in response"
        assert isinstance(new_post[BODY], str), "'body' should be a string"
        assert new_post[BODY] == NEW_POST[BODY], "Body does not match posted body"

    def test_post_posts_missing_fields(self):
        """
        Test case: Creating a post with missing required fields (e.g., no 'title' or 'userId').
        JSONPlaceholder still simulates a successful creation with 201 Created.
        """
        resp = self.client.create_post(POST_MISSING_FIELDS)

        # JSONPlaceholder fakes a successful post creation even if fields are missing
        assert resp.status_code == HTTPStatus.CREATED, f"Expected 201 Created, got {resp.status_code}"

    def test_post_posts_empty_post(self):
        """
        Test case: Creating an entirely empty post (no payload).
        JSONPlaceholder still responds with 201 Created and generates a post.
        """
        resp = self.client.create_post(NULL_POST)

        # Even an empty post returns 201 — this reflects JSONPlaceholder’s simulation logic
        assert resp.status_code == HTTPStatus.CREATED, f"Expected 201 Created, got {resp.status_code}"
