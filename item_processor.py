from .api_service import ApiService
from .data_service import DataService

class ItemProcessor:
    def __init__(self, api_service: ApiService, data_service: DataService):
        self.api_service = api_service
        self.data_service = data_service

    def process_associate_emails_by_dg(self, items_endpoint: str, details_endpoint: str, dgname: str, headers: dict = None, details_params: dict = None, verify: bool = True):
        items = self.api_service.get_associate_emails_by_dg(items_endpoint, dgname, headers, verify)
        item_details_list = []

        for item in items:
            item_id = item['id']
            details = self.api_service.request_item_details(details_endpoint, item_id, headers, details_params, verify)
            item_details_list.append(details)

        dataframe = self.data_service.json_to_dataframe(item_details_list)
        return dataframe
