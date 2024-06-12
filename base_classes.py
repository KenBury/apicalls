from abc import ABC, abstractmethod
import pandas as pd

class DataService(ABC):
    @abstractmethod
    def load_data(self) -> (pd.DataFrame, pd.DataFrame):
        pass

    @abstractmethod
    def filter_data(self, families: pd.DataFrame, individuals: pd.DataFrame, family_names: list) -> (pd.DataFrame, pd.DataFrame):
        pass

    @abstractmethod
    def merge_data(self, families: pd.DataFrame, individuals: pd.DataFrame) -> pd.DataFrame:
        pass

class ExcelService(ABC):
    @abstractmethod
    def export(self, dataframe: pd.DataFrame, export_type: str, column_headings: list, additional_data: list = None):
        pass
