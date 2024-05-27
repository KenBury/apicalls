from .api_service import ApiServiceImpl
from .data_service import DataServiceImpl
from .item_processor import ItemProcessor

def main():
    base_url = "https://api.example.com"
    api_service = ApiServiceImpl(base_url)
    data_service = DataServiceImpl()

    items_endpoint = "associates"
    details_endpoint = "associates"
    dgname = "dgname_value"  # Specify the dgname here
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Accept": "application/json"
    }  # Add any necessary headers for the requests
    details_params = {}  # Add any necessary parameters for the item details request
    verify = False  # Set to False to skip SSL verification (use with caution)

    processor = ItemProcessor(api_service, data_service)
    dataframe = processor.process_associate_emails_by_dg(items_endpoint, details_endpoint, dgname, headers, details_params, verify)

    print(dataframe)

if __name__ == "__main__":
    main()
