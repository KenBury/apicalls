import pandas as pd

class DataService:
    def json_to_dataframe(self, json_data: list) -> pd.DataFrame:
        """
        Converts a list of JSON objects to a Pandas DataFrame.

        Parameters:
        json_data (list): List of JSON objects to convert.

        Returns:
        pd.DataFrame: DataFrame containing the data.
        """
        return pd.DataFrame(json_data)

class DataServiceImpl(DataService):
    pass
