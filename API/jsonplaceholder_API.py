import requests


class JSONPlaceholderAPI:
    """
    A thin wrapper around JSONPlaceholder’s /posts endpoints.
    """

    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self.base_url = base_url.rstrip("/")

    def get_posts(self) -> requests.Response:
        """Retrieve the list of all posts."""
        return requests.get(f"{self.base_url}/posts")

    def get_post(self, post_id) -> requests.Response:
        """Retrieve a single post by ID."""
        return requests.get(f"{self.base_url}/posts/{post_id}")

    def create_post(self, payload: dict) -> requests.Response:
        """Create a new post."""
        return requests.post(f"{self.base_url}/posts", json=payload)

    def update_post(self, post_id, payload: dict) -> requests.Response:
        """Update an existing post by ID."""
        return requests.put(f"{self.base_url}/posts/{post_id}", json=payload)

    def delete_post(self, post_id) -> requests.Response:
        """Delete a post by ID."""
        return requests.delete(f"{self.base_url}/posts/{post_id}")
