import requests

class ApiClient:
  """Base class for making API calls"""

  def __init__(self, base_url):
    self.base_url = base_url

  def _make_request(self, method, endpoint, **kwargs):
    """Makes an API request with common logic"""
    url = f"{self.base_url}/{endpoint}"
    response = requests.request(method, url, **kwargs)
    response.raise_for_status()  # Raise exception for non-2xx status codes
    return response.json()

  def get(self, endpoint):
    """Makes a GET request to a specific endpoint"""
    return self._make_request("GET", endpoint)

  def post(self, endpoint, data):
    """Makes a POST request to a specific endpoint with data"""
    return self._make_request("POST", endpoint, json=data)

  # You can add other methods like put, delete etc. following the same pattern

class UsersApi(ApiClient):
  """Derived class for interacting with the users endpoint"""

  def __init__(self, base_url):
    super().__init__(base_url)

  def get_all_users(self):
    """Gets a list of all users"""
    return self.get("users")

  def get_user_by_id(self, user_id):
    """Gets a specific user by ID"""
    return self.get(f"users/{user_id}")

class PostsApi(ApiClient):
  """Derived class for interacting with the posts endpoint"""

  def __init__(self, base_url):
    super().__init__(base_url)

  def create_post(self, data):
    """Creates a new post"""
    return self.post("posts", data)

  def get_post_by_id(self, post_id):
    """Gets a specific post by ID"""
    return self.get(f"posts/{post_id}")

# Usage example
base_url = "https://api.example.com"
users_api = UsersApi(base_url)
posts_api = PostsApi(base_url)

all_users = users_api.get_all_users()
user = users_api.get_user_by_id(123)

new_post_data = {"title": "My New Post", "content": "This is some content"}
new_post = posts_api.create_post(new_post_data)

print(all_users)
print(user)
print(new_post)
