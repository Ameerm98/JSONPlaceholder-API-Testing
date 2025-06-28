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
POST_MISSING_FIELDS_ID = '12'
NULL_POST = {}
INVALID_POST_ID = '-5ADAD'
NON_EXIST_POST_ID = '105'
NEGATIVE_POST_ID = '-2'
DELETE_POST_ID = '6'

