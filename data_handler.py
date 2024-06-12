import pandas as pd
from base_classes import DataHandler

class PickleDataHandler(DataHandler):
    def __init__(self, family_file_path, individual_file_path):
        self.family_file_path = family_file_path
        self.individual_file_path = individual_file_path

    def load_data(self) -> (pd.DataFrame, pd.DataFrame):
        families = pd.read_pickle(self.family_file_path)
        individuals = pd.read_pickle(self.individual_file_path)
        return families, individuals

    def filter_data(self, families: pd.DataFrame, individuals: pd.DataFrame, family_names: list) -> (pd.DataFrame, pd.DataFrame):
        filtered_families = families[families['family_name'].isin(family_names)]
        filtered_individuals = individuals[individuals['family_id'].isin(filtered_families['family_id'])]
        return filtered_families, filtered_individuals

    def merge_data(self, families: pd.DataFrame, individuals: pd.DataFrame) -> pd.DataFrame:
        merged_df = pd.merge(individuals, families, on='family_id', suffixes=('_individual', '_family'))
        # Concatenate birthdate and death date (if available) with a newline separator
        merged_df['birthdate'] = merged_df['birthdate'].astype(str)
        merged_df['deathdate'] = merged_df['deathdate'].astype(str)
        merged_df['birthdate_deathdate'] = merged_df['birthdate'] + '\n' + merged_df['deathdate'].replace('nan', '', regex=True)
        # Select required columns and reorder
        final_df = merged_df[['family_name', 'individual_name', 'birthdate_deathdate']]
        final_df = final_df.sort_values(by=['family_name', 'individual_name'])
        return final_df
