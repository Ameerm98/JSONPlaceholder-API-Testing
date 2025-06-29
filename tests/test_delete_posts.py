import pytest
from http import HTTPStatus
from API.jsonplaceholder_API import JSONPlaceholderAPI
from tests.data.tests_data import (
    DELETE_POST_ID,
    NON_EXIST_POST_ID,
    NEGATIVE_POST_ID,
    INVALID_POST_ID
)


def get_api_client():
    """Return an instance of the JSONPlaceholder API client."""
    return JSONPlaceholderAPI()


class TestDELETEPosts:
    client = get_api_client()

    def test_delete_posts_id(self):
        """
        Test deleting a post with a valid post ID.
        Even though JSONPlaceholder doesn't persist data,
        the API simulates successful deletion with a 200 OK.
        """
        resp = self.client.delete_post(DELETE_POST_ID)

        # Expect 200 OK for a successful (simulated) delete
        assert resp.status_code == HTTPStatus.OK, f"Expected 200 OK for delete, got {resp.status_code}"

    def test_delete_non_exist_post(self):
        """
        Test deleting a post with a non-existent (but valid-format) post ID.
        JSONPlaceholder still returns 200 OK to simulate idempotent deletion.
        """
        resp = self.client.delete_post(NON_EXIST_POST_ID)

        # Still expect 200 OK — deletion should be idempotent even if the ID doesn't exist
        assert resp.status_code == HTTPStatus.OK, f"Expected 200 OK for delete, got {resp.status_code}"

    def test_delete_invalid_id_post(self):
        """
        Test deleting a post with an invalid (malformed) ID — e.g., string or special characters.
        JSONPlaceholder still returns 200 OK.
        """
        resp = self.client.delete_post(INVALID_POST_ID)

        # Even for malformed ID, JSONPlaceholder simulates 200 OK — note for test coverage
        assert resp.status_code == HTTPStatus.OK, f"Expected 200 OK for delete, got {resp.status_code}"

    def test_delete_negative_id_post(self):
        """
        Test deleting a post with a negative ID.
        JSONPlaceholder also returns 200 OK in this edge case.
        """
        resp = self.client.delete_post(NEGATIVE_POST_ID)

        # Expect 200 OK, confirming simulated behavior is idempotent regardless of input
        assert resp.status_code == HTTPStatus.OK, f"Expected 200 OK for delete, got {resp.status_code}"
