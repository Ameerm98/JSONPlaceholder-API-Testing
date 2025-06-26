from http import HTTPStatus
import requests
import pytest


class TestJSONPlaceholderAPI:
    # TESTS DATA #
    BASE_URL = "https://jsonplaceholder.typicode.com"

    # Post Fields
    USER_ID = "userId"
    ID = "id"
    TITLE = "title"
    BODY = "body"

    # Valid post
    VALID_POST_ID = 1
    VALID_POST_USER_ID = 1
    POST_TITLE = "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    POST_BODY = "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"

    # New Post
    NEW_POST_TITLE = "API TESTING"
    NEW_POST_ID = 101
    NEW_POST = {
        "userid": "250298",
        "id": "101",
        "title": "API TESTING",
        "body": "Post Endpoint"
    }

    # Updated Post
    UPDATE_POST_ID = '2'
    UPDATED_POST_TITLE = "updated title"
    UPDATED_POST_BODY = "updated body"
    UPDATE_POST = {
        "id": 2,
        "userId": 2,
        "title": "updated title",
        "body": "updated body"
    }

    POST_MISSING_FIELDS = {"body": "incomplete"}

    INVALID_POST_ID = '-5ADAD'

    DELETE_POST_ID = '26000'

    """Test case - retrieving all posts."""
    def test_get_posts(self):
        response = requests.get(self.BASE_URL + "/posts")
        status_code = response.status_code
        posts = response.json()

        assert status_code == HTTPStatus.OK, f"Expected 200 OK, got {status_code}"
        assert isinstance(posts, list), "Expected response content to be a list of posts"

    """Test case - retrieving a single post by valid ID."""
    def test_get_posts_with_valid_id(self):
        response = requests.get(self.BASE_URL + "/posts/" + str(self.VALID_POST_ID))
        status_code = response.status_code
        valid_post = response.json()

        assert status_code == HTTPStatus.OK, f"Expected 200 OK, got {status_code}"
        assert isinstance(valid_post, dict), "Expected response content to be a single post (dict)"

        assert self.USER_ID in valid_post, "'userId' key is missing in the response"
        assert isinstance(valid_post[self.USER_ID], int), "'userId' should be an integer"
        assert valid_post[
                   self.USER_ID] == self.VALID_POST_ID, f"Expected userId {self.VALID_POST_ID}, got {valid_post[self.USER_ID]}"

        assert self.ID in valid_post, "'id' key is missing in the response"
        assert isinstance(valid_post[self.ID], int), "'id' should be an integer"
        assert valid_post[self.ID] == self.VALID_POST_ID, f"Expected id {self.VALID_POST_ID}, got {valid_post[self.ID]}"

        assert self.TITLE in valid_post, "'title' key is missing in the response"
        assert isinstance(valid_post[self.TITLE], str), "'title' should be a string"
        assert valid_post[self.TITLE] == self.POST_TITLE, "Title does not match expected value"

        assert self.BODY in valid_post, "'body' key is missing in the response"
        assert isinstance(valid_post[self.BODY], str), "'body' should be a string"
        assert valid_post[self.BODY] == self.POST_BODY, "Body does not match expected value"

    """Test case - retrieving a post with an invalid ID."""
    def test_get_posts_invalid_id(self):
        response = requests.get(self.BASE_URL + "/posts/" + self.INVALID_POST_ID)
        status_code = response.status_code

        assert status_code == HTTPStatus.NOT_FOUND, f"Expected 404 Not Found, got {status_code}"

    """Test case - creating a new post."""
    def test_post_posts(self):
        response = requests.post(self.BASE_URL + "/posts", json=self.NEW_POST)
        status_code = response.status_code
        new_post = response.json()

        assert status_code == HTTPStatus.CREATED, f"Expected 201 Created, got {status_code}"
        assert isinstance(new_post, dict), "Expected response to be a dict"

        assert self.ID in new_post, "'id' key missing in response"
        assert isinstance(new_post[self.ID], int), "'id' should be an integer"
        assert new_post[self.ID] == self.NEW_POST_ID, f"Expected id {self.NEW_POST_ID}, got {new_post[self.ID]}"

        assert self.TITLE in new_post, "'title' key missing in response"
        assert isinstance(new_post[self.TITLE], str), "'title' should be a string"
        assert new_post[self.TITLE] == self.NEW_POST_TITLE, "Title does not match posted title"

        assert self.BODY in new_post, "'body' key missing in response"
        assert isinstance(new_post[self.BODY], str), "'body' should be a string"
        assert new_post[self.BODY] == self.NEW_POST[self.BODY], "Body does not match posted body"

    """Test case - updating a post with missing fields."""
    def test_put_posts_missing_fields(self):
        response = requests.put(self.BASE_URL + "/posts", json=self.POST_MISSING_FIELDS)
        status_code = response.status_code
        assert status_code == HTTPStatus.NOT_FOUND, f"Expected 404 Not Found, got {status_code}"

    """Test case - updating a specific post with given valid id."""
    def test_put_posts_id(self):
        response = requests.put(self.BASE_URL + "/posts/" + self.UPDATE_POST_ID, json=self.UPDATE_POST)
        status_code = response.status_code
        updated_post = response.json()

        assert status_code == HTTPStatus.OK, f"Expected 200 OK, got {status_code}"
        assert isinstance(updated_post, dict), "Expected updated post to be a dict"

        assert updated_post[self.ID] == self.UPDATE_POST[self.ID], "ID does not match updated value"
        assert updated_post[self.USER_ID] == self.UPDATE_POST[self.USER_ID], "userId does not match updated value"
        assert updated_post[self.TITLE] == self.UPDATED_POST_TITLE, "Title does not match updated value"
        assert updated_post[self.BODY] == self.UPDATED_POST_BODY, "Body does not match updated value"

    """Test case - deleting a post with valid id."""
    def test_delete_posts_id(self):
        response = requests.delete(self.BASE_URL + "/posts/" + self.DELETE_POST_ID)
        status_code = response.status_code

        assert status_code == HTTPStatus.OK, f"Expected 200 OK for delete, got {status_code}"

        followup_response = requests.get(self.BASE_URL + "/posts/" + self.DELETE_POST_ID)
        followup_status = followup_response.status_code

        assert followup_status == HTTPStatus.NOT_FOUND, f"Expected 404 Not Found after delete, got {followup_status}"
