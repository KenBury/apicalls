from abc import ABC, abstractmethod
import requests

class ApiService(ABC):
    @abstractmethod
    def request_workEmails_by_dgname(self, endpoint: str, dgname: str, headers: dict = None, params: dict = None, verify: bool = True) -> list:
        pass

    @abstractmethod
    def request_item_details(self, endpoint: str, item_id: int, headers: dict = None, params: dict = None, verify: bool = True) -> list:
        pass

class ApiServiceImpl(ApiService):
    def __init__(self, base_url: str):
        self.base_url = base_url

    def request_workEmails_by_dgname(self, endpoint: str, dgname: str, headers: dict = None, params: dict = None, verify: bool = True) -> list:
        items = []
        url = f"{self.base_url}/{endpoint}"
        
        # Include the dgname in the query parameters
        if params is None:
            params = {}
        params['dgname'] = dgname
        
        while url:
            response = requests.get(url, headers=headers, params=params, verify=verify)
            response.raise_for_status()
            data = response.json()
            items.extend(data['results'])
            url = data.get('next')  # Assuming the paginated response uses 'next' for the next page URL
            params = None  # Reset params after the first request
        
        return items

    def request_item_details(self, endpoint: str, item_id: int, headers: dict = None, params: dict = None, verify: bool = True) -> list:
        details = []
        url = f"{self.base_url}/{endpoint}/{item_id}/details"
        
        while url:
            response = requests.get(url, headers=headers, params=params, verify=verify)
            response.raise_for_status()
            data = response.json()
            details.extend(data['results'])
            url = data.get('next')  # Assuming the paginated response uses 'next' for the next page URL
            params = None  # Reset params after the first request
        
        return details
