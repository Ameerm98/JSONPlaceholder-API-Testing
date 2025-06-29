import pytest
from http import HTTPStatus
from API.jsonplaceholder_API import JSONPlaceholderAPI
from API import utils
from tests.data.tests_data import (
    UPDATE_POST,
    UPDATED_POST_BODY,
    UPDATED_POST_TITLE,
    UPDATE_POST_ID,
    POST_MISSING_FIELDS,
    POST_MISSING_FIELDS_ID,
    USER_ID,
    ID,
    TITLE,
    BODY
)


def get_api_client():
    """Return an instance of the JSONPlaceholder API client."""
    return JSONPlaceholderAPI()


class TestPUTPosts:
    client = get_api_client()

    def test_put_posts_id(self):
        """
        Test case: Updating a post with a valid ID and a complete update payload.
        This is a full replacement using PUT — the API should return the updated post.
        """
        resp = self.client.update_post(UPDATE_POST_ID, UPDATE_POST)
        updated_post = utils.get_response_content(resp)

        # Ensure the update succeeded with HTTP 200 OK
        assert resp.status_code == HTTPStatus.OK, f"Expected 200 OK, got {resp.status_code}"

        # Response should be a dictionary containing the updated post
        assert isinstance(updated_post, dict), "Expected updated post to be a dict"

        # Validate that the ID remains the same as sent in the payload
        assert updated_post[ID] == UPDATE_POST[ID], "ID does not match updated value"

        # Validate that the userId remains the same as the original post
        assert updated_post[USER_ID] == UPDATE_POST[USER_ID], "userId does not match updated value"

        # Validate that the title has been updated correctly
        assert updated_post[TITLE] == UPDATED_POST_TITLE, "Title does not match updated value"

        # Validate that the body has been updated correctly
        assert updated_post[BODY] == UPDATED_POST_BODY, "Body does not match updated value"

    def test_put_posts_missing_fields(self):
        """
        Test case: Updating a post with a payload that includes only partial data.
        JSONPlaceholder simulates successful updates even with missing fields.
        """
        resp = self.client.update_post(POST_MISSING_FIELDS_ID, POST_MISSING_FIELDS)

        # JSONPlaceholder returns 200 OK even if required fields are missing in the PUT payload
        assert resp.status_code == HTTPStatus.OK, f"Expected 200 OK, got {resp.status_code}"
